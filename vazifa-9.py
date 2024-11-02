import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = arr[len(arr) // 2]
    left = [x for x in arr if x < mid]
    middle = [x for x in arr if x == mid]
    right = [x for x in arr if x > mid]
    return quick_sort(left) + middle + quick_sort(right)

random_list = [random.randint(1, 1000) for _ in range(100)]


start_time = time.time()
bubble_sort(random_list.copy())
bubble_sort_time = time.time() - start_time

start_time = time.time()
quick_sort(random_list.copy())
quick_sort_time = time.time() - start_time

print("Bubble Sort vaqti:", bubble_sort_time)
print("Quick Sort vaqti:", quick_sort_time)
