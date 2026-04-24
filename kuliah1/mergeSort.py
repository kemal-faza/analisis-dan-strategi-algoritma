from typing import List


def mergeSort(array: List[int], i: int, j: int):
    if i < j:
        mid = (i + j) // 2
        mergeSort(array, i, mid)
        mergeSort(array, mid + 1, j)
        merge(array, i, mid, j)


def merge(array: List[int], low: int, mid: int, high: int):
    result: List[int] = [0] * len(array)

    pivot1: int = low
    pivot2: int = mid + 1
    i = low

    while pivot1 <= mid and pivot2 <= high:
        if array[pivot1] <= array[pivot2]:
            result[i] = array[pivot1]
            pivot1 += 1
        else:
            result[i] = array[pivot2]
            pivot2 += 1
        i += 1

    while pivot1 <= mid:
        result[i] = array[pivot1]
        pivot1 += 1
        i += 1

    while pivot2 <= high:
        result[i] = array[pivot2]
        pivot2 += 1
        i += 1

    for i in range(low, high + 1):
        array[i] = result[i]


randomList = list(map(int, input().split()))

mergeSort(randomList, 0, len(randomList) - 1)
print(randomList)
