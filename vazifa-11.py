def quick_uzunlik(arr):
    if len(arr) <= 1:
        return arr
    pivot = len(arr[len(arr) // 2])
    left = [x for x in arr if len(x) < pivot]
    middle = [x for x in arr if len(x) == pivot]
    right = [x for x in arr if len(x) > pivot]
    return quick_uzunlik(left) + middle + quick_uzunlik(right)

lists = ["olma", "banan", "behi", "anor"]
print("Natija:", quick_uzunlik(lists))
