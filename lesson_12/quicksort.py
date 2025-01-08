def quicksort(arr: list):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Опорний елемент

    left = [i for i in arr if i < pivot]  # [4, 1, 2, 1, 0]
    middle = [i for i in arr if i == pivot]  # [6]
    right = [i for i in arr if i > pivot]  # [23]

    return quicksort(left) + middle + quicksort(right)


arr = [4, 23, 1, 6, 2, 1, 0]

print(quicksort(arr))
