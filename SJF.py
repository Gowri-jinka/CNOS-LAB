def calculate_times(processes, burst_times):
    n = len(burst_times)
    wt = [0] * n  # Waiting time
    tat = [0] * n  # Turnaround time

    # Sort processes by burst time
    for i in range(n):
        for k in range(i + 1, n):
            if burst_times[i] > burst_times[k]:
                burst_times[i], burst_times[k] = burst_times[k], burst_times[i]
                processes[i], processes[k] = processes[k], processes[i]

    # Calculating waiting time
    for i in range(1, n):
        wt[i] = wt[i - 1] + burst_times[i - 1]

    # Calculating turnaround time
    for i in range(n):
        tat[i] = wt[i] + burst_times[i]

    return wt, tat

def print_scheduling_result(processes, burst_times, wt, tat):
    n = len(burst_times)
    print("\tPROCESS\tBURST TIME\tWAITING TIME\tTURNAROUND TIME")
    for i in range(n):
        print(f"\tP{processes[i]}\t\t{burst_times[i]}\t\t{wt[i]}\t\t{tat[i]}")

    wtavg = sum(wt) / n
    tatavg = sum(tat) / n
    print(f"\nAverage Waiting Time -- {wtavg:.6f}")
    print(f"Average Turnaround Time -- {tatavg:.6f}")

# Main function
def main():
    n = int(input("Enter the number of processes -- "))
    processes = list(range(n))
    burst_times = []
    for i in range(n):
        bt = int(input(f"Enter Burst Time for Process {i} -- "))
        burst_times.append(bt)

    wt, tat = calculate_times(processes, burst_times)
    print_scheduling_result(processes, burst_times, wt, tat)

if __name__ == "__main__":
    main()
