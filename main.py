import scheduler

TOTAL_MEMORY = 1024  # Memeory available in MB

def load_processes_from_file(filename):
    """
    Reads process data from file (PID,ArrivalTime,BurstTime,Memory).
    """
    processes = []
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                if not line.strip() or line.strip().startswith('#'):
                    continue
                parts = line.strip().split(',')
                if len(parts) != 4:
                    print(f"Warning: Line {line_num}: malformed ({len(parts)} parts)")
                    continue
                try:
                    pid     = parts[0].strip()
                    arrival = int(parts[1].strip())
                    burst   = int(parts[2].strip())
                    memory  = int(parts[3].strip())
                    if arrival < 0 or burst <= 0 or memory <= 0:
                        print(f"Warning: Line {line_num}: invalid values")
                        continue
                    processes.append({
                        'pid': pid,
                        'arrival_time': arrival,
                        'burst_time': burst,
                        'memory': memory
                    })
                except ValueError:
                    print(f"Warning: Line {line_num}: non-numeric data")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

    if not processes:
        print("Error: No valid processes loaded.")
        return None
    return processes

def main():
    print("--- OS Simulator ---")
    processes_data = load_processes_from_file('processes.txt')
    if not processes_data:
        print("Exiting due to errors.")
        return

    print(f"Loaded {len(processes_data)} processes.")
    print(f"Memory: {TOTAL_MEMORY} MB")

    while True:
        algorithm = input("Enter scheduling algorithm (fcfs / sjf): ").lower()
        if algorithm in ('fcfs', 'sjf'):
            break
        print("Invalid choice.")

    sim = scheduler.Scheduler(processes_data, TOTAL_MEMORY)
    print(f"--- Running {algorithm.upper()} ---")
    sim.run(algorithm)
    sim.display_performance_metrics()
    print("--- Simulation Complete ---")

if __name__ == "__main__":
    main()
