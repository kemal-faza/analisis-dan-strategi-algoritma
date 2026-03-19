n = int(input())
listPoinNakal = list(map(int, input().split()))


def mergeAndCount(subList, tempList, left, mid, right):
    i = left
    j = mid + 1
    k = left
    counterError = 0

    while i <= mid and j <= right:
        if subList[i] <= subList[j]:
            tempList[k] = subList[i]
            i += 1
        else:
            tempList[k] = subList[j]
            counterError += mid - i + 1
            j += 1
        k += 1

    while i <= mid:
        tempList[k] = subList[i]
        i += 1
        k += 1

    while j <= right:
        tempList[k] = subList[j]
        j += 1
        k += 1

    indeks = left
    while indeks <= right:
        subList[indeks] = tempList[indeks]
        indeks += 1

    return counterError


def dividePoin(subList, tempList, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    countErrorKiri = dividePoin(subList, tempList, left, mid)
    countErrorKanan = dividePoin(subList, tempList, mid + 1, right)
    countErrorSilang = mergeAndCount(subList, tempList, left, mid, right)

    return countErrorKiri + countErrorKanan + countErrorSilang


tempList = [0] * n
print(dividePoin(listPoinNakal, tempList, 0, n - 1))
