def reverse_integer(i):
    if i < 0:
        res = int(str(i)[1:][::-1]) * -1
    else:
        res = int(str(i)[::-1])
    if -(2**31) > res or res > 2**31 - 1:
        return 0
    return res


nums = 123
resoult = reverse_integer(nums)
print(resoult)
