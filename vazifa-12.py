def unique_sorted(arr):
    elementlar = list(set(arr))
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        mid = arr[len(arr) // 2]
        left = [x for x in arr if x < mid]
        middle = [x for x in arr if x == mid]
        right = [x for x in arr if x > mid]
        return quick_sort(left) + middle + quick_sort(right)
    
    return quick_sort(elementlar)

arr = [4, 4, 2, 2, 9, 1, 1, 3]
print(unique_sorted(arr))
