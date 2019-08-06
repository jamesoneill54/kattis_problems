# https://open.kattis.com/problems/froshweek2
import sys

def frosh_week():
    lines = []
    for idx, line in enumerate(sys.stdin):
        if idx > 0:
            formatted_line = [int(time) for time in line.strip().split()]
            formatted_line.sort()
            lines.append(formatted_line)
    task_times, available_times = lines
    tasks_accomplished = 0
    task_idx, time_idx = 0, 0
    while task_idx < len(task_times) and time_idx < len(available_times):
        if task_times[task_idx] <= available_times[time_idx]:
            tasks_accomplished += 1
            task_idx += 1
        time_idx += 1
    return tasks_accomplished

if __name__ == "__main__":
    print(frosh_week())
