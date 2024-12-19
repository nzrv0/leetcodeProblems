def sqrt_of_x(x):
    if x == 0:
        return x
    first, last = 1, x
    while first <= last:
        mid = (first + last) // 2
        if x // mid == mid:
            return mid
        elif x // mid < mid:
            last = mid - 1
        else:
            first = mid + 1
    return last


x = 9

resoult = sqrt_of_x(x)
print(resoult)
