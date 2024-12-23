def arrange(n):
    i = 0
    while n >= 0:
        i += 1
        n -= i
    return i - 1


n = 8
res = arrange(n)
print(res)
