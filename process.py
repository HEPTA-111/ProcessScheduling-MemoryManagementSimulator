class Process:
    """
    Represents a process in the simulation, holding its attributes and statistics.
    """
    def __init__(self, pid, arrival_time, burst_time, memory):
        # Basic attributes
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.memory = memory

        # Statistics
        self.start_time = -1
        self.completion_time = -1
        self.waiting_time = -1
        self.turnaround_time = -1

        # Memory management
        self.memory_start_address = -1

    def calculate_metrics(self):
        """
        Calculates waiting and turnaround times after completion_time is set.
        """
        if self.completion_time != -1:
            self.turnaround_time = self.completion_time - self.arrival_time
            self.waiting_time = self.turnaround_time - self.burst_time
        else:
            print(f"Warning: Metrics calculated for process {self.pid} before completion.")

    def __repr__(self):
        return (f"Process(pid={self.pid}, arrival={self.arrival_time}, "
                f"burst={self.burst_time}, memory={self.memory})")
