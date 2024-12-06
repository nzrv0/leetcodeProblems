def missing(nums):
    new_nums = list(range(min(nums), max(nums) + 1))
    res = list(set(new_nums) - set(nums))
    if len(res) > 0:
        return res[0]
    elif min(nums) == 0:
        return max(nums) + 1
    else:
        return 0


nums = [1, 2, 3]
res = missing(nums)
print(res)
