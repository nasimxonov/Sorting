def linear_sort(arr, x):
    count = 0
    for num in arr:
        if num == x:
            count += 1
    return count

lists = [5, 2, 3, 9, 5, 5, 1]
x = 5
print(f"Natija: Son {x} uchrash soni:", linear_sort(lists, x))
