def binarySearch(array, i, j, k):
    if i > j:
        return -1
    else:
        mid = (i + j) // 2
        if k < array[mid]:
            return binarySearch(array, i, mid - 1, k)
        elif k > array[mid]:
            return binarySearch(array, mid + 1, j, k)
        else:
            return mid


listAngka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binarySearch(listAngka, 0, len(listAngka) - 1, int(input())))
