# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1

n, a, b = map(int, input().split())


def fung(n, a, b):
    if n == 0:
        return a
    if n == 1:
        return b

    dp = [0] * (n + 1)
    dp[0], dp[1] = a, b

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(fung(n, a, b))
