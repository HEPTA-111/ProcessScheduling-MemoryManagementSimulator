

## 1. Project Overview

This project is a Python-based simulator created for the B206 Operating Systems module. Its purpose is to implement and analyze core operating system concepts in a practical setting. The simulator models the execution of processes in a single-CPU environment, focusing on the interplay between CPU scheduling and contiguous memory allocation.

The primary goal is to compare the performance of two non-preemptive scheduling algorithms—First-Come, First-Served (FCFS) and Shortest-Job-First (SJF)—to observe their impact on system performance metrics like waiting time and turnaround time.

---

## 2. OS Concepts Implemented

This project demonstrates the following key Operating Systems concepts:

* **Process Management:**
    * **Process Representation:** Processes are modeled as objects with states and attributes (PID, Arrival Time, Burst Time), simulating a Process Control Block (PCB).
    * **Process Scheduling:** Implementation and comparison of FCFS and SJF scheduling algorithms.
    * **Process Queues:** Management of a ready queue to hold processes waiting for CPU allocation.

* **Memory Management:**
    * **Contiguous Allocation:** The system simulates a single block of main memory.
    * **First-Fit Algorithm:** Implements the First-Fit strategy for allocating memory blocks to processes.
    * **Memory Deallocation & Merging:** Handles the freeing of memory upon process completion and merges adjacent free blocks to reduce external fragmentation.

---

## 3. Project File Structure

The project is organized into the following files for clarity and modularity:

* `main.py`: The main entry point for the application. It handles user interaction (selecting the algorithm) and loading the initial process data from `processes.txt`.
* `scheduler.py`: Contains the core simulation logic. The `Scheduler` class manages the simulation clock, the ready queue, the execution of processes, and the memory management (allocation/deallocation) logic.
* `process.py`: Defines the `Process` class, which acts as a blueprint for each process, storing its attributes and calculated performance statistics.
* `processes.txt`: A simple text file used to define the workload for the simulation. Users can edit this file to test the simulator with different sets of processes.
* `README.md`: This documentation file.

---

## 4. Setup and Execution Instructions

To run this simulator, you will need Python 3 installed. The following steps guide you through setting up a virtual environment and running the project from a PowerShell terminal.

### Step 1: Set Up the Environment

1.  **Clone the repository or download the files** into a project folder.Here is the repo link (https://github.com/delxnkD/ProcessScheduling-MemoryManagementSimulator.git)

2.  **Open PowerShell** and navigate to your project directory:
    ```powershell
    cd path\to\your\project\folder
    ```
3.  **Create a Python virtual environment**:
    ```powershell
    python -m venv venv
    ```
4.  **Activate the virtual environment**:
    ```powershell
    .\venv\Scripts\Activate
    ```
    *(Your terminal prompt should now be prefixed with `(venv)`)*

### Step 2: Run the Simulator

1.  Ensure the `processes.txt` file is in the same directory and contains the process data you wish to simulate.
2.  Execute the `main.py` script from your terminal:
    ```powershell
    python main.py
    ```
3.  The program will start and prompt you to choose a scheduling algorithm. Type `fcfs` or `sjf` and press Enter.

    ![Program Execution](https://placehold.co/700x150/2d3748/ffffff?text=C:\Project>+python+main.py\nEnter+scheduling+algorithm+(fcfs/sjf):+sjf)

4.  The simulator will then run, printing a detailed log of events (process arrivals, execution, memory allocation, and completions) followed by a final performance summary.


