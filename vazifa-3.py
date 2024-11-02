def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            for j in range(i, n - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

lists = [1, 2, 3, 8, 6, 5]
print("Natija:", bubble_sort(lists))
