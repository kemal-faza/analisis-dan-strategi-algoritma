n, m = map(int, input().split())
listRuang = list(map(int, input().split()))
prefixSum = []

listNomorLama = []
for i in range(m):
    listNomorLama.append(int(input()))

totalRuang = 0
for ruang in listRuang:
    totalRuang += ruang
    prefixSum.append(totalRuang)


def binarySearch(prefixSum, target):
    low = 0
    high = ans = len(prefixSum) - 1
    while low <= high:
        mid = (low + high) // 2
        if prefixSum[mid] >= target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


for nomorLama in listNomorLama:
    indeksLantai = binarySearch(prefixSum, nomorLama)
    nomorLantai = indeksLantai + 1

    if indeksLantai == 0:
        nomorRuang = nomorLama
    else:
        nomorRuang = nomorLama - prefixSum[indeksLantai - 1]

    print(nomorLantai, nomorRuang)
