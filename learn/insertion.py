import random as r
import time as t

def insertion_sort(arr):
    t_start = t.time()
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        arr[position] = current_value
    t_end = t.time()
    print(t_end-t_start)
    return arr

arr = list(range(1, 1001))
r.shuffle(arr)
print(insertion_sort(arr))

