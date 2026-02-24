# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
arr.reverse()

print(arr[0] + arr[1])
