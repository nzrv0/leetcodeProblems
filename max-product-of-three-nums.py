def product_nums(nums):
    nums.sort()
    print(nums)
    return max(nums[-3] * nums[-2] * nums[-1], nums[-1] * nums[0] * nums[1])


nums = [-100, -98, -1, 2, 3, 4]
res = product_nums(nums)
print(res)
