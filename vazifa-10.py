def quick_sort(arr, low, high, n):
    if low < high:
        mid = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < mid:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pi = i + 1
        
        
        if pi < n - 1:
            quick_sort(arr, pi + 1, high, n)
        quick_sort(arr, low, pi - 1, n)

def tartib(arr, n):
    quick_sort(arr, 0, len(arr) - 1, n)
    return arr

arr = [45, 22, 76, 33, 18, 50]
n = 3
print(tartib(arr, n))  
