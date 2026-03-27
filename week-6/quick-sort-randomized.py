# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1

from random import randint


n = int(input())
listAngka = list(map(int, input().split()))


def swap(listAngka, i, j):
    listAngka[i], listAngka[j] = listAngka[j], listAngka[i]


def partition(listAngka, low, high, isFirst):
    if isFirst:
        randomIndex = randint(low, high)
        swap(listAngka, randomIndex, high)

    pivot = listAngka[high]
    i = low - 1
    for j in range(low, high):
        if listAngka[j] <= pivot:
            i += 1
            swap(listAngka, i, j)

    swap(listAngka, i + 1, high)
    return i + 1


def quickSort(listAngka, low, high, isFirst):
    if low < high:
        pivotIndex = partition(listAngka, low, high, isFirst)
        quickSort(listAngka, low, pivotIndex - 1, False)
        quickSort(listAngka, pivotIndex + 1, high, False)


quickSort(listAngka, 0, len(listAngka) - 1, True)
print(*listAngka)
