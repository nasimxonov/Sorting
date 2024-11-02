def quick_bubble(arr):
    mid = arr[-1]
    left = [x for x in arr if x < mid]
    right = [x for x in arr if x > mid]
    
    for i in range(len(left) - 1):
        for j in range(len(left) - 1 - i):
            if left[j] > left[j + 1]:
                left[j], left[j + 1] = left[j + 1], left[j]
                
    for i in range(len(right) - 1):
        for j in range(len(right) - 1 - i):
            if right[j] > right[j + 1]:
                right[j], right[j + 1] = right[j]
    
    return left + [mid] + right

arr = [15, 20, 5, 12, 10, 1]
print(quick_bubble(arr))  
