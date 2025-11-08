import matplotlib.pyplot as plt
import random
import time #unused import

def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            plt.clf()
            plt.bar(range(len(arr)), arr, color="skyblue")
            plt.title(f"{j}&{j+1}")
            #time.sleep(0.001)
            plt.pause(0.01)
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    plt.clf()
    plt.bar(range(len(arr)), arr, color="limegreen")
    plt.show()

data = [random.randint(1, 50) for _ in range(20)]
plt.ion()
bubble_sort_visual(data)
