def partition(nums, start, end):
    pivot = nums[start]
    left = start
    right = end

    while left != right:
        while left < right and nums[right] >= pivot:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <pivot:
            left += 1
        nums[right] = nums[left]

    nums[left] = pivot
    return left


def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot_index = partition(nums, start, end)
    quick_sort(nums, start, pivot_index - 1)
    quick_sort(nums, pivot_index + 1, end)


if __name__ == '__main__':
    nums = [23, 4, 1, 523, 2, 3, 111]
    quick_sort(nums, 0, 6)
    print(nums)
