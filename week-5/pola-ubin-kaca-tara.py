n, m = map(int, input().split())
matriksUbin = []

for i in range(n):
    matriksUbin.append(list(map(int, input().split())))


def cekSimteris(n, m):
    ukuranMatriks = n * m
    left, right = 0, ukuranMatriks - 1
    while left < right:
        rowAwal = left // m
        colAwal = left % m
        rowAkhir = right // m
        colAkhir = right % m

        if matriksUbin[rowAwal][colAwal] == matriksUbin[rowAkhir][colAkhir]:
            left += 1
            right -= 1
        else:
            return False
    return True


print("RAPI") if cekSimteris(n, m) else print("TIDAK")
