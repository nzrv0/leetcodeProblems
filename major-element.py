# time compleaxty O(n)
def major_element(nums):
    default_dict = {}
    major_elem = res = 0
    for num in nums:
        default_dict[num] = 1 + default_dict.get(num, 0)
        if major_elem < default_dict[num]:
            major_elem = default_dict[num]
            res = num

    return res


nums = [6, 5, 5]
resoult = major_element(nums)

# time compleaxty O(1)


def major_element2(nums):
    major_element = res = 0

    for num in nums:
        if major_element == 0:
            res = num
        major_element += 1 if num == res else -1
