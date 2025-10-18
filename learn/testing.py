import random as r
import time

sorted_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unsorted_arr = list(range(1, 11))
r.shuffle(unsorted_arr)

def bubble_sort(arr):
    time_start = time.time()
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # print(arr)
    time_end = time.time()
    print("Bubble sort")
    print("Сорт", arr)
    print(time_end-time_start, "секунд")

def is_sorted(sorted_arr, unsorted_arr):
    if sorted_arr == unsorted_arr:
        return True
    else:
        return False

def bogosort(sorted_arr, sorting_arr):
    start_time = time.time()
    attempts = 0

    while not is_sorted(sorted_arr, sorting_arr):
        r.shuffle(sorting_arr)
        attempts +=1
    
    end_time = time.time()

    print("Bogosort")
    print(sorting_arr)
    print(end_time-start_time, "секунд")
    print(attempts, "попыток")

bubble_sort(unsorted_arr)

unsorted_arr = list(range(1, 11))
r.shuffle(unsorted_arr)

bogosort(sorted_arr, unsorted_arr)