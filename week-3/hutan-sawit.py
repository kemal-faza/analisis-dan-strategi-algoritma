n, maxEmas = map(int, input().split())
listEmas = list(map(int, input().split()))
emasDibawa = 0


def max2(n1, n2):
    return n1 if n1 > n2 else n2


def hutanSawit(currentEmas, index):
    global emasDibawa
    if currentEmas > maxEmas:
        return

    if index == n:
        emasDibawa = max2(emasDibawa, currentEmas)
        return

    hutanSawit(currentEmas + listEmas[index], index + 1)
    hutanSawit(currentEmas, index + 1)


hutanSawit(0, 0)
print(emasDibawa)
