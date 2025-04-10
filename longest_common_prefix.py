def longestCommonPrefix(strs):
    max_len = len(max(strs))

    ll = ""
    res = ""
    if len(strs) == 1:
        return strs[0]

    for j in range(max_len):
        for i in strs:
            if len(i) - 1 < j:
                return res
            ll += i[j]
        if len(set(ll)) != 1:
            return res

        res += ll[0]
        ll = ""
    return res


strs = ["flower", "flow", "flight"]
strs = ["dog", "racecar", "car"]

# strs = ["", "b"]
# strs = ["ab", "a"]
# strs = ["a", "b"]
res = longestCommonPrefix(strs)


print(res)
