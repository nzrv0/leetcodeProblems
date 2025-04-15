def climbing_stairs(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = dp[1] = 1
    print(dp)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


n = 4
# 1. 2 + 2
# 2. 1 + 2 + 1
# 3. 2 + 1 + 1
# 4. 1 + 1 + 2
# 5. 1 + ...
res = climbing_stairs(n)
print(res)


n = 5
# 3. 2 + 1 + 1 + 1
# 2. 1 + 2 + 1 + 1
# 4. 1 + 1 + 2 + 1
# 4. 1 + 1 + 1 + 2
# 2 + 2 + 1
# 1 + 2 + 2
# 2 + 1 + 2
# 5. 1 + ...
