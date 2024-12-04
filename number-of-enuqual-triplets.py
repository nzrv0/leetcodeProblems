def uniqual(nums):
    nums.sort()
    unice = list(set(nums))
    ex = {}
    ss = []

    for num in nums:
        ex[num] = 1 + ex.get(num, 0)
    for item in ex.keys():
        if ex[max(ex.keys())] != 1:
            ss.append(item)

        ex[item] -= 1
    print(ss)
    return len(ss)
    # res = 0
    # if len(unice) <= 1:
    #     return 0

    # if max(nums) > len(nums):
    #     unice.pop()

    # if len(unice) == 2:
    #     return 1

    # while res < min(nums) and min(nums) >= 2:
    #     res += 1

    # return res + 1


nums = [1000, 999, 998]
resoult = uniqual(nums)
print(resoult)
