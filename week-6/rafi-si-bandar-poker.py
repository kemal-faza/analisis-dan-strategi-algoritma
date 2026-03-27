# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1

n = int(input())
listAngka = list(map(int, input().split()))
worstIteration = -1
bestIteration = float("inf")
worstValue = None
bestValue = None


def swap(listAngka, i, j):
    listAngka[i], listAngka[j] = listAngka[j], listAngka[i]


def partition(listAngka, low, high):
    pivot = listAngka[high]
    i = low - 1
    for j in range(low, high):
        if listAngka[j] <= pivot:
            i += 1
            swap(listAngka, i, j)

    swap(listAngka, i + 1, high)
    return i + 1


def quickSort(listAngka, low, high):
    global iterator
    iterator += 1
    if low < high:
        pivotIndex = partition(listAngka, low, high)
        quickSort(listAngka, low, pivotIndex - 1)
        quickSort(listAngka, pivotIndex + 1, high)


for i in range(n):
    listUrut = listAngka[:]
    swap(listUrut, i, n - 1)

    iterator = 0
    quickSort(listUrut, 0, n - 1)

    if iterator > worstIteration:
        worstIteration = iterator
        worstValue = listAngka[i]

    if iterator < bestIteration:
        bestIteration = iterator
        bestValue = listAngka[i]

print(worstValue)
print(bestValue)
