# priority queue + greedy
import heapq
from itertools import count
from multiprocessing import heap

def append_to_heap(heap, task, count):
    count += 1
    if count < 0:
        heapq.heappush(heap, (count, task))
    else: 
        heapq.heappop(heap)

def task_scheduler(heap, n):
    # greedy approach to schedule tasks
    temp = []
    while heap: 
        for _ in range(n):
            if heap:
                # abjad ascii check 
                count, task = heap[0]
                try: 
                    if count < 0 and (ord(task) < ord(temp[-1])):
                        temp.append(task)
                        append_to_heap(heap, task, count)
                    else:
                        heapq.heappop(heap)
                        continue
                except IndexError:
                    append_to_heap(heap, task, count)
            else:
                break 
            # idle = ascii 0
            temp.append(chr(0))

    return len(temp)

def initialize_heap(tasks):
    # initialize heap with task counts
    task_counts = {}
    for task in tasks:
        if task in task_counts:
            task_counts[task] += 1
        else:
            task_counts[task] = 1

    heap = []
    for task, count in task_counts.items():
        heapq.heappush(heap, (-count, task))
    
    return heap

heap = initialize_heap(["A","A","A","B","B","B"])
print(task_scheduler(heap, 2))
print(task_scheduler(initialize_heap(["A","C","A","B","D","B"]), 1))
print(task_scheduler(initialize_heap(["A","A","A", "B","B","B"]), 3))