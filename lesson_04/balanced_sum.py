def find_balancing_index(arr):
    for x in arr:
        if x < 0:
            return -1

    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum = left_sum + arr[i]

    return -1
