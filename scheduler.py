import process

class Scheduler:
    """
    Manages simulation: process queues, clock, memory, and metrics.
    """
    def __init__(self, processes_data, total_memory):
        self.processes = sorted(
            [process.Process(**p) for p in processes_data],
            key=lambda p: p.arrival_time
        )
        self.total_memory = total_memory
        self.free_memory_blocks = [(0, total_memory)]
        self.time = 0
        self.ready_queue = []
        self.completed_processes = []
        self.running_process = None

    def _allocate_memory(self, required_memory):
        for i, (start, size) in enumerate(self.free_memory_blocks):
            if size >= required_memory:
                allocated_start = start
                if size > required_memory:
                    self.free_memory_blocks[i] = (
                        start + required_memory, size - required_memory
                    )
                else:
                    self.free_memory_blocks.pop(i)
                print(f"[{self.time}] Allocated {required_memory}MB at {allocated_start}")
                return allocated_start
        return None

    def _deallocate_memory(self, start_address, size):
        self.free_memory_blocks.append((start_address, size))
        self.free_memory_blocks.sort()
        merged = []
        cur_start, cur_size = self.free_memory_blocks[0]
        for next_start, next_size in self.free_memory_blocks[1:]:
            if cur_start + cur_size == next_start:
                cur_size += next_size
            else:
                merged.append((cur_start, cur_size))
                cur_start, cur_size = next_start, next_size
        merged.append((cur_start, cur_size))
        self.free_memory_blocks = merged
        print(f"[{self.time}] Deallocated {size}MB at {start_address}. Free: {self.free_memory_blocks}")

    def run(self, algorithm):
        process_queue = list(self.processes)
        while process_queue or self.ready_queue or self.running_process:
            while process_queue and process_queue[0].arrival_time <= self.time:
                p = process_queue.pop(0)
                self.ready_queue.append(p)
                print(f"[{self.time}] Arrival: Process {p.pid}")

            if not self.running_process and self.ready_queue:
                if algorithm == 'sjf':
                    self.ready_queue.sort(key=lambda p: p.burst_time)
                for i, p in enumerate(self.ready_queue):
                    addr = self._allocate_memory(p.memory)
                    if addr is not None:
                        self.running_process = self.ready_queue.pop(i)
                        self.running_process.start_time = self.time
                        self.running_process.memory_start_address = addr
                        print(f"[{self.time}] Running: Process {p.pid}")
                        break

            self.time += 1

            rp = self.running_process
            if rp and self.time >= rp.start_time + rp.burst_time:
                rp.completion_time = self.time
                rp.calculate_metrics()
                self._deallocate_memory(rp.memory_start_address, rp.memory)
                self.completed_processes.append(rp)
                print(f"[{self.time}] Completion: Process {rp.pid}")
                self.running_process = None

    def display_performance_metrics(self):
        if not self.completed_processes:
            print("No completed processes.")
            return

        self.completed_processes.sort(key=lambda p: p.pid)
        n = len(self.completed_processes)
        total_wt = sum(p.waiting_time for p in self.completed_processes)
        total_tt = sum(p.turnaround_time for p in self.completed_processes)

        print("\n--- Metrics ---")
        print(f"{'PID':<5}{'Arr':<5}{'Bur':<5}{'Cmp':<5}{'Wtg':<5}{'TAT'}")
        print("-" * 40)
        for p in self.completed_processes:
            print(f"{p.pid:<5}{p.arrival_time:<5}{p.burst_time:<5}"
                  f"{p.completion_time:<5}{p.waiting_time:<5}{p.turnaround_time}")

        print(f"\nAvg Waiting Time: {total_wt/n:.2f}")
        print(f"Avg Turnaround Time: {total_tt/n:.2f}")
