# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2

n = int(input())
kelelahanDasar = list(map(int, input().split()))
kelelahanTambahan = [list(map(int, input().split())) for _ in range(n)]
hasil = sum(kelelahanDasar)

if n > 1:
    minimumTambahan = [float("inf")]
    dikunjungi = [False] * n

    def cekKombinasi(prev, count, totalTambahanSementara):
        if count == n:
            if totalTambahanSementara < minimumTambahan[0]:
                minimumTambahan[0] = totalTambahanSementara
            return

        for current in range(n):
            if not dikunjungi[current]:
                dikunjungi[current] = True
                biayaKelelahan = kelelahanTambahan[current][prev]
                cekKombinasi(
                    current, count + 1, totalTambahanSementara + biayaKelelahan
                )
                dikunjungi[current] = False

    for start in range(n):
        dikunjungi[start] = True
        cekKombinasi(start, 1, 0)
        dikunjungi[start] = False

    hasil += minimumTambahan[0]

print(hasil)
