# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2
n = int(input())
arr = list(map(int, input().split()))
energiDiPerlukan = 0

arr.sort()

mid = n // 2

target = arr[mid]

for i in range(n):
    energiDiPerlukan += abs(arr[i] - target)

print(energiDiPerlukan)
