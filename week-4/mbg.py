n = int(input())
listKalori = list(map(int, input().split()))


def mergeSort(subList):
    if len(subList) <= 1:
        return subList

    mid = len(subList) // 2
    left = mergeSort(subList[:mid])
    right = mergeSort(subList[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[i])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def divideKalori(subList):
    sortedList = mergeSort(subList)

    print(sortedList[0], sortedList[-1])


divideKalori(listKalori)
