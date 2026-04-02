def min2(a, b):
    if a < b:
        return a
    else:
        return b

def max2(a, b):
    if a > b:
        return a
    else:
        return b

def MBG(arr, kiri, kanan):
    if kiri == kanan:
        return arr[kiri], arr[kiri]
    elif kanan - kiri == 1:
        if arr[kiri] < arr[kanan]:
            return arr[kiri], arr[kanan]
        else:
            return arr[kanan], arr[kiri]
    else:
        # Divide: array dibagi jadi 2 bagian
        tengah = (kiri + kanan) // 2

        minKiri, maxKiri = MBG(arr, kiri, tengah)
        minKanan, maxKanan = MBG(arr, tengah + 1, kanan)

        # Conquer/Combine: hasil min-max dari kiri dan kanan digabung
        mini = min2(minKiri, minKanan)
        maks = max2(maxKiri, maxKanan)

        return mini, maks

n = int(input())
arr = list(map(int, input().split()))

mini, maks = MBG(arr, 0, n - 1)
print(mini, maks)


def isiKiri(arr, temp, i, k, tengah):
    if i > tengah:
        return
    else:
        temp[k] = arr[i]
        isiKiri(arr, temp, i + 1, k + 1, tengah)

def isiKanan(arr, temp, j, k, kanan):
    if j > kanan:
        return
    else:
        temp[k] = arr[j]
        isiKanan(arr, temp, j + 1, k + 1, kanan)

def gabungRekursif(arr, temp, i, j, k, tengah, kanan):
    if i > tengah:
        isiKanan(arr, temp, j, k, kanan)
        return 0
    elif j > kanan:
        isiKiri(arr, temp, i, k, tengah)
        return 0
    else:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            return gabungRekursif(arr, temp, i + 1, j, k + 1, tengah, kanan)
        else:
            temp[k] = arr[j]
            # Saat elemen kanan lebih kecil, semua sisa elemen kiri membentuk error
            return (tengah - i + 1) + gabungRekursif(arr, temp, i, j + 1, k + 1, tengah, kanan)

def salinBalik(arr, temp, kiri, kanan):
    if kiri > kanan:
        return
    else:
        arr[kiri] = temp[kiri]
        salinBalik(arr, temp, kiri + 1, kanan)

def gabung(arr, temp, kiri, tengah, kanan):
    error = gabungRekursif(arr, temp, kiri, tengah + 1, kiri, tengah, kanan)
    salinBalik(arr, temp, kiri, kanan)
    return error

def Lele(arr, temp, kiri, kanan):
    if kiri >= kanan:
        return 0
    else:
        # Divide: pecah array jadi 2 bagian
        tengah = (kiri + kanan) // 2

        errorKiri = Lele(arr, temp, kiri, tengah)
        errorKanan = Lele(arr, temp, tengah + 1, kanan)

        # Combine: gabungkan dua bagian terurut sambil hitung error silang
        errorGabung = gabung(arr, temp, kiri, tengah, kanan)

        return errorKiri + errorKanan + errorGabung

n = int(input())
arr = list(map(int, input().split()))
temp = [0] * n

print(Lele(arr, temp, 0, n - 1))




def Rafi(arr, kiri, kanan, x, jawab):
    if kiri > kanan:
        return jawab
    else:
        # Divide: ruang pencarian dibelah dua
        tengah = (kiri + kanan) // 2

        if arr[tengah] >= x:
            # Kalau tengah sudah memenuhi, jawaban mungkin ada lebih kiri
            # Jadi lanjut cari ke bagian kiri
            return Rafi(arr, kiri, tengah - 1, x, tengah + 1)
        else:
            # Kalau tengah belum memenuhi, buang kiri dan cari di kanan
            return Rafi(arr, tengah + 1, kanan, x, jawab)

n, q = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(q):
    x = int(input())
    print(Rafi(arr, 0, n - 1, x, -1))



def buatPrefix(lantai, prefix, i, n, jumlah):
    if i == n:
        return
    else:
        jumlah += lantai[i]
        prefix.append(jumlah)
        buatPrefix(lantai, prefix, i + 1, n, jumlah)

def cariLantai(prefix, kiri, kanan, x, jawab):
    if kiri > kanan:
        return jawab
    else:
        tengah = (kiri + kanan) // 2

        if prefix[tengah] >= x:
            # Decrease: kalau prefix tengah sudah cukup,
            # lanjut kecilkan ke kiri untuk cari lantai pertama yang cocok
            return cariLantai(prefix, kiri, tengah - 1, x, tengah)
        else:
            # Decrease: kalau masih kurang, buang sisi kiri
            return cariLantai(prefix, tengah + 1, kanan, x, jawab)

def prosesQuery(prefix, n, sisa):
    if sisa == 0:
        return
    else:
        x = int(input())
        idx = cariLantai(prefix, 0, n - 1, x, -1)

        if idx == 0:
            nomor = x
        else:
            nomor = x - prefix[idx - 1]

        print(idx + 1, nomor)
        prosesQuery(prefix, n, sisa - 1)

n, m = map(int, input().split())
lantai = list(map(int, input().split()))

prefix = []
buatPrefix(lantai, prefix, 0, n, 0)

prosesQuery(prefix, n, m)


def isiKiri(arr, temp, i, k, tengah):
    if i > tengah:
        return
    else:
        temp[k] = arr[i]
        isiKiri(arr, temp, i + 1, k + 1, tengah)

def isiKanan(arr, temp, j, k, kanan):
    if j > kanan:
        return
    else:
        temp[k] = arr[j]
        isiKanan(arr, temp, j + 1, k + 1, kanan)

def gabungRekursif(arr, temp, i, j, k, tengah, kanan):
    if i > tengah:
        isiKanan(arr, temp, j, k, kanan)
    elif j > kanan:
        isiKiri(arr, temp, i, k, tengah)
    else:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            gabungRekursif(arr, temp, i + 1, j, k + 1, tengah, kanan)
        else:
            temp[k] = arr[j]
            gabungRekursif(arr, temp, i, j + 1, k + 1, tengah, kanan)

def salinBalik(arr, temp, kiri, kanan):
    if kiri > kanan:
        return
    else:
        arr[kiri] = temp[kiri]
        salinBalik(arr, temp, kiri + 1, kanan)

def gabung(arr, temp, kiri, tengah, kanan):
    gabungRekursif(arr, temp, kiri, tengah + 1, kiri, tengah, kanan)
    salinBalik(arr, temp, kiri, kanan)

def urutkan(arr, temp, kiri, kanan):
    if kiri >= kanan:
        return
    else:
        tengah = (kiri + kanan) // 2

        # Divide: array dibagi jadi 2 bagian
        urutkan(arr, temp, kiri, tengah)
        urutkan(arr, temp, tengah + 1, kanan)

        # Combine: dua bagian terurut digabung jadi satu bagian terurut
        gabung(arr, temp, kiri, tengah, kanan)

def hitungBisa(arr, kiri, kanan, stamina, jawab):
    if kiri > kanan:
        return jawab
    else:
        tengah = (kiri + kanan) // 2

        if arr[tengah] <= stamina:
            # Decrease: kalau rak tengah masih bisa diperiksa,
            # cari kemungkinan lebih banyak di kanan
            return hitungBisa(arr, tengah + 1, kanan, stamina, tengah + 1)
        else:
            # Decrease: kalau terlalu sulit, kecilkan ke kiri
            return hitungBisa(arr, kiri, tengah - 1, stamina, jawab)

def prosesHari(hari, i, m, rak, n, total):
    if i == m:
        return total
    else:
        return prosesHari(hari, i + 1, m, rak, n, total + hitungBisa(rak, 0, n - 1, hari[i], 0))

n, m = map(int, input().split())
rak = list(map(int, input().split()))
hari = list(map(int, input().split()))

temp = [0] * n
urutkan(rak, temp, 0, n - 1)

print(prosesHari(hari, 0, m, rak, n, 0))

def cekUbin(mat, m, kiri, kanan):
    if kiri >= kanan:
        return "RAPI"
    else:
        r1 = kiri // m
        c1 = kiri % m

        r2 = kanan // m
        c2 = kanan % m

        if mat[r1][c1] != mat[r2][c2]:
            return "TIDAK"
        else:
            # Decrease: masalah diperkecil dari dua ujung menuju tengah
            return cekUbin(mat, m, kiri + 1, kanan - 1)

n, m = map(int, input().split())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

print(cekUbin(mat, m, 0, n * m - 1))