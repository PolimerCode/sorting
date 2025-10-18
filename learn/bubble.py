arr = [5, 2, 4, 1]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print("if part", arr)
            print("1", arr)
        print("2", arr)
    print("final result:", arr)

bubble_sort(arr)