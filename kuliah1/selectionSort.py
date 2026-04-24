def selectionSort(array, i, j):
    if i < j:
        bagi(array, i, j)
        selectionSort(array, i + 1, j)


def bagi(array, i, j):
    indeksMin = i
    for k in range(i + 1, j + 1):
        if array[k] < array[indeksMin]:
            indeksMin = k

    print(f"{i=} {array[i]=} {indeksMin=} {array[indeksMin]=}")

    temp = array[i]
    array[i] = array[indeksMin]
    array[indeksMin] = temp


listAngka = list(map(int, input().split()))
selectionSort(listAngka, 0, len(listAngka) - 1)
print(listAngka)
