# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2
n, m, x = map(int, input().split())
listMobil = []
totalHargaSewa = float("inf")

for i in range(n):
    listMobil.append(list(map(int, input().split())))


def exploreMobil(index, total_Pi, total_Vi, total_Ci):
    global totalHargaSewa
    if total_Ci >= totalHargaSewa:
        return

    if total_Vi >= x and total_Pi >= m:
        totalHargaSewa = total_Ci
        return

    if index >= n:
        return

    exploreMobil(
        index + 1,
        total_Pi + listMobil[index][0],
        total_Vi + listMobil[index][1],
        total_Ci + listMobil[index][2],
    )
    exploreMobil(index + 1, total_Pi, total_Vi, total_Ci)


exploreMobil(0, 0, 0, 0)

print(totalHargaSewa if totalHargaSewa != float("inf") else -1)
