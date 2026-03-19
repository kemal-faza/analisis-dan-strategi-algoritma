n, q = map(int, input().split())
listDamage = list(map(int, input().split()))
listSituasi = []

for i in range(q):
    listSituasi.append(int(input()))


for i in range(q):
    left = 0
    right = n - 1
    indeksSenjata = -1

    while left <= right:

        mid = (left + right) // 2

        if listDamage[mid] >= listSituasi[i]:
            indeksSenjata = mid
            right = mid - 1

        elif listDamage[mid] < listSituasi[i]:
            left = mid + 1

    print(indeksSenjata + 1) if indeksSenjata != -1 else print(indeksSenjata)
