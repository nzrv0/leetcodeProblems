def search_position(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] < target:
            left = mid + 1

        elif nums[mid] > target:
            right = mid - 1
    return left


nums = [1, 3, 5, 6]
target = 2
res = search_position(nums, target)
print(res)
