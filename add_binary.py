def add_binary(a, b):
    # max_len = a if len(a) > len(b) else b
    # res = []
    # for i in range(1, len(max_len) + 1):
    #     rr = b if max_len == a else a

    #     if len(rr) + 1 != i:
    #         if int(max_len[-i]) == 1 and int(rr[-i]) == 1:
    #             res.insert(0, "0")
    #             res.insert(0, "1")
    #         else:
    #             res.insert(0, str(int(max_len[-i]) | int(rr[-i])))
    #     else:
    #         if int(max_len[-i]) == 1 and int(res[0]) == 1:
    #             res[0] = "0"
    #         res.insert(0, max_len[-i])

    # return res
    current = 0
    argA, argB = len(a) - 1, len(b) - 1
    res = []
    while argA >= 0 or argB >= 0 or current == 1:
        if argA >= 0:
            current += int(a[argA])
            argA -= 1
        if argB >= 0:
            current += int(b[argB])
            argB -= 1

        res.append(str(current % 2))
        current = current // 2
    return "".join(res[::-1])


a = "1111"

b = "1011"

["1", "0"]
res = add_binary(a, b)
print(res)

# "11010"
