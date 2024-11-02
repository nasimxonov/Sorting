def kichik_count(arr):
    average = sum(arr) / len(arr)
    count = 0
    for num in arr:
        if num < average:
            count += 1
    return count

lists = [10, 12, 15, 20, 25]
print("Natija:", kichik_count(lists))
