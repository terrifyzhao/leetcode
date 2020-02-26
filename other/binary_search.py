def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


a = [1, 2, 3, 4, 5, 6, 7]
res = binary_search(a, 6)
print(res)
