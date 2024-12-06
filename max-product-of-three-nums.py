def product_nums(nums):
    # nn = sorted(list(map(lambda x: x * -1 if x < 0 else x, nums)), reverse=True)

    # res = 1
    # nums.sort()
    # print(nums)
    # ll = map(lambda x: -1 if x < 0 else 1, nums)
    # for i in nn[:3]:
    #     res *= i
    #     print(i)
    mm = 0
    ll = []
    res = 1
    for num in nums:
        print(mm, num)
        if num < 0 and num * -1 > mm:
            mm = num * -1
        else:
            mm = num
        ll.append(num)
    for i in ll[::-1][:3]:
        res *= i
    print(res)


nums = [-100, -98, -1, 2, 3, 4]
res = product_nums(nums)
print(res)
