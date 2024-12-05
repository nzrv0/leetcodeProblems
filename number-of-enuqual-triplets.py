from collections import Counter


def uniqual(nums):
    c = Counter(nums)

    res = 0
    left = 0
    right = len(nums)

    for _, freq in c.items():
        right -= freq
        res += left * freq * right
        left += freq
    return res


nums = [1, 1, 1]
resoult = uniqual(nums)
print(resoult)
