# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1

from random import randint

import numpy as np


n = int(input())
listAngka = np.array(list(map(int, input().split())))
listAngkaCopy = listAngka.copy()
iterasi = iteration = 0


def swap(listAngka, i, j):
    listAngka[i], listAngka[j] = listAngka[j], listAngka[i]


def partition(listAngka, low, high, isFirst):
    global iteration
    if isFirst:
        # randomIndex = randint(low, high)
        # print(listAngka[randomIndex])
        # swap(listAngka, randomIndex, high)
        swap(listAngka, iteration, high)
        iteration += 1

    pivot = listAngka[high]
    i = low - 1
    for j in range(low, high):
        if listAngka[j] <= pivot:
            i += 1
            swap(listAngka, i, j)
        print(f"{pivot=} {i=} {j=} {listAngka=} {low=} {high=}")

    swap(listAngka, i + 1, high)
    return i + 1


def quickSort(listAngka, low, high, isFirst):
    global iterasi
    if low < high:
        iterasi += 1
        pivotIndex = partition(listAngka, low, high, isFirst)
        quickSort(listAngka, low, pivotIndex - 1, False)
        quickSort(listAngka, pivotIndex + 1, high, False)


while iteration != n:
    iterasi = 0
    listAngka = listAngkaCopy.copy()
    quickSort(listAngka, 0, len(listAngka) - 1, True)
    print(f"{listAngka=} {iterasi=}\n")
