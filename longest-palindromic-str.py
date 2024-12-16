def longestPalindrome(s):
    res = ""
    count = 0
    ss = []
    if len(set(s)) == 1:
        return s
    for i in range(len(s)):
        for j in range(count, len(s)):
            res += s[j]
            if res == res[::-1]:
                ss.append(res)
            if j + 1 == len(s):
                count += 1
                res = ""
    return max(ss, key=len)


example = "cbbd"
resoult = longestPalindrome(example)
print(resoult)
