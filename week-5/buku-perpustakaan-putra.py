n, m = map(int, input().split())

listRak = list(map(int, input().split()))
listStamina = list(map(int, input().split()))


def insertionSort(listRak):
    for i in range(1, len(listRak)):
        key = listRak[i]
        j = i - 1
        while j >= 0 and listRak[j] > key:
            listRak[j + 1] = listRak[j]
            j -= 1
        listRak[j + 1] = key
    return listRak


def binarySearch(listRak, target):
    low = 0
    high = len(listRak) - 1
    ans = len(listRak)

    while low <= high:
        mid = (low + high) // 2
        if listRak[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


listRak = insertionSort(listRak)
totalBuku = 0
for stamina in listStamina:
    totalBuku += binarySearch(listRak, stamina)

print(totalBuku)
