# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2
n = int(input())
arr = list(map(int, input().split()))
listGanjil = []
listGenap = []

arr.sort()
arr.reverse()

for i in range(n):
    if arr[i] % 2 == 0:
        listGenap.append(arr[i])
    else:
        listGanjil.append(arr[i])

if len(listGanjil) < 2:
    print(-1)
else:
    if len(listGenap) != 0:
        print(max(sum(listGanjil[0:2] + [listGenap[0]]), sum(listGanjil[0:3])))
    else:
        print(sum(listGanjil[0:3]))
