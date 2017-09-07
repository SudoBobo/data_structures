from queue import PriorityQueue

procN, taskN = map(int, input().split(' '))
tasks_times = [int(task_time) for task_time in input().split(' ')]


# to store processing tasks in format [time_when_proccessing_ends, proc_idx]
pq = PriorityQueue()
# to store answer in format [proc_idx, time_when_proccessing_started]
proc_log = []

curr_time = 0
# handle border cases

if procN == 1:
    for task_idx in range(taskN):
        print(0, curr_time)
        curr_time = curr_time + tasks_times[task_idx]
elif procN >= taskN:
    for task_idx in range(taskN):
        print(task_idx, 0)

else:
    # fill queue with first m tasks
    for proc_idx in range(procN):
        pq.put([curr_time + tasks_times[proc_idx], proc_idx])
        proc_log.append([proc_idx, curr_time])

    for task_idx in range(procN, taskN):
        # extract finished task and process number it's been handled. Change time
        free_proc = pq.get()
        curr_time = free_proc[0]

        # log
        proc_log.append([free_proc[1], curr_time])
        # add new task
        free_proc[0] = curr_time + tasks_times[task_idx]
        pq.put(free_proc)

    for elem in proc_log:
        print(*elem)