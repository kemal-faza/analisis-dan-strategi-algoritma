# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1

n, t = map(int, input().split())
dp = [0] * (t + 1)

for _ in range(n):
    waktu, kepentingan, kesulitan, latihan = map(int, input().split())

    nilai = (kepentingan * 10) + (latihan * 5) - (kesulitan * 2)

    for w in range(t, waktu - 1, -1):
        dp[w] = max(dp[w], dp[w - waktu] + nilai)


print(dp[t])
