n, x = map(int, input().split())
listPity = []
jumlahSSR = 0
minimumPull = 0

for i in range(n):
    listPity.append(list(map(int, input().split())))


def min2(n1, n2):
    return n1 if n1 < n2 else n2


def countSSR(index, pity):
    global jumlahSSR, minimumPull

    if index == n:
        if jumlahSSR < x:
            minimumPull = -1
        return

    if pity >= min2(listPity[index][0], listPity[index][1]) - 1:
        jumlahSSR += 1
        pity = 0
    else:
        pity += 1

    if jumlahSSR >= x:
        minimumPull = index + 1
        return

    countSSR(index + 1, pity)


countSSR(0, 0)
print(minimumPull)
