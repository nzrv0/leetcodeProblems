def maxiumum(nums):
    nn = list(dict.fromkeys(sorted(nums, reverse=True)))
    return nn[0:3][2] if len(dict.fromkeys(nums)) > 2 else nn[0]


nums = [-1, 2, 3]
res = maxiumum(nums)
print(res)
