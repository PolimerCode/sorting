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
    print(arr)
    print(t_end-t_start)
    return arr

arr = list(range(1, 100001))
r.shuffle(arr)
insertion_sort(arr)

# 205.48200583457947 seconds for 100000 numbers random shuffled list
