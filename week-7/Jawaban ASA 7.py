
#2
def dfs(awal, p, status, posisi, jawaban):
    # jalur menyimpan urutan teman yang dilewati
    # saat DFS dimulai dari node awal
    jalur = []

    node = awal

    # Selama node belum pernah dikunjungi,
    # terus lanjut mengikuti arah p[node]
    while status[node] == 0:
        # Tandai node sedang berada di jalur DFS sekarang
        status[node] = 1

        # Simpan posisi node di dalam jalur
        # Ini berguna kalau nanti ditemukan siklus
        posisi[node] = len(jalur)

        # Masukkan node ke jalur
        jalur.append(node)

        # Lanjut ke teman yang ditunjuk node ini
        node = p[node]

    # Jika berhenti di node dengan status 1,
    # berarti node tersebut sudah ada di jalur DFS sekarang
    # Jadi kita menemukan siklus
    if status[node] == 1:
        # awalSiklus adalah indeks pertama node siklus di dalam jalur
        awalSiklus = posisi[node]

        # Semua node dari awalSiklus sampai akhir jalur adalah bagian siklus
        for i in range(awalSiklus, len(jalur)):
            teman = jalur[i]

            # Jika mulai dari node siklus,
            # node pertama yang mendapat tanda kedua adalah dirinya sendiri
            jawaban[teman] = teman

        # Untuk node sebelum siklus,
        # jawabannya mengikuti jawaban dari node tujuannya
        for i in range(awalSiklus - 1, -1, -1):
            teman = jalur[i]
            tujuan = p[teman]

            jawaban[teman] = jawaban[tujuan]

    else:
        # Jika status[node] == 2,
        # berarti node ini sudah selesai diproses sebelumnya
        # Maka semua node di jalur sekarang tinggal mengikuti
        # jawaban dari node tujuannya
        for i in range(len(jalur) - 1, -1, -1):
            teman = jalur[i]
            tujuan = p[teman]

            jawaban[teman] = jawaban[tujuan]

    # Setelah semua jawaban untuk jalur ini didapat,
    # tandai semua node di jalur sebagai sudah selesai
    for teman in jalur:
        status[teman] = 2


# Program utama
n = int(input())

data = list(map(int, input().split()))

# p[i] = teman yang ditunjuk oleh teman i
p = [0] * (n + 1)

for i in range(1, n + 1):
    p[i] = data[i - 1]

# status[i]:
# 0 = belum dikunjungi
# 1 = sedang berada di jalur DFS sekarang
# 2 = sudah selesai diproses
status = [0] * (n + 1)

# posisi[i] = posisi node i di dalam jalur DFS
# Jika node tidak sedang berada di jalur, nilainya tidak penting
posisi = [-1] * (n + 1)

# jawaban[i] = teman pertama yang mendapat tanda kedua
# jika Gege mulai dari teman i
jawaban = [0] * (n + 1)

# Jalankan DFS dari setiap node yang belum diproses
for i in range(1, n + 1):
    if status[i] == 0:
        dfs(i, p, status, posisi, jawaban)

# Cetak jawaban untuk setiap kemungkinan teman awal
for i in range(1, n + 1):
    print(jawaban[i])

#3
def dfsKomponen(graf, awal, dalamKomponen):
    # Fungsi ini dipakai untuk mencari semua node/topik
    # yang masih berada dalam satu komponen dengan node awal S.
    # Karena graph tidak berarah, jika sebuah node bisa dicapai dari S,
    # maka node tersebut masih satu komponen dengan S.
    # tumpukan digunakan untuk DFS secara iteratif
    # agar tidak terkena recursion limit jika N sangat besar
    tumpukan = []

    # Masukkan node awal ke dalam tumpukan
    tumpukan.append(awal)

    # Tandai node awal sebagai bagian dari komponen S
    dalamKomponen[awal] = True

    # Selama masih ada node yang perlu diproses
    while len(tumpukan) > 0:
        # Ambil node paling atas dari tumpukan
        node = tumpukan.pop()

        # Cek semua tetangga dari node ini
        for tetangga in graf[node]:

            # Jika tetangga belum pernah dikunjungi
            if dalamKomponen[tetangga] == False:

                # Tandai tetangga sebagai bagian dari komponen S
                dalamKomponen[tetangga] = True

                # Masukkan tetangga ke tumpukan
                # supaya nanti tetangganya juga ikut dicek
                tumpukan.append(tetangga)


def bfsTerjauh(graf, awal, dalamKomponen, n):
    # Fungsi ini dipakai untuk mencari node/topik
    # yang jaraknya paling jauh dari node awal S.
    # Karena yang dicari adalah jarak terpendek,
    # maka algoritma yang tepat adalah BFS.

    # jarak[i] menyimpan jarak terpendek dari node awal ke node i
    #
    # Nilai -1 artinya node belum pernah dikunjungi oleh BFS
    jarak = [-1] * (n + 1)

    # Queue manual tanpa deque
    # antrian menyimpan node-node yang akan diproses
    antrian = []

    # depan menunjukkan indeks node yang sedang diproses dalam antrian
    depan = 0

    # Masukkan node awal ke antrian
    antrian.append(awal)

    # Jarak dari node awal ke dirinya sendiri adalah 0
    jarak[awal] = 0

    # jawabanNode menyimpan node dengan jarak paling jauh sejauh ini
    jawabanNode = awal

    # jawabanJarak menyimpan jarak terjauh sejauh ini
    jawabanJarak = 0

    # Selama masih ada node dalam antrian yang belum diproses
    while depan < len(antrian):

        # Ambil node dari bagian depan antrian
        node = antrian[depan]
        depan += 1

        # Jika jarak node ini lebih jauh dari jawaban saat ini,
        # maka node ini menjadi jawaban baru
        if jarak[node] > jawabanJarak:
            jawabanJarak = jarak[node]
            jawabanNode = node

        # Jika jaraknya sama dengan jarak terjauh,
        # pilih node dengan nomor yang lebih kecil
        elif jarak[node] == jawabanJarak and node < jawabanNode:
            jawabanNode = node

        # Cek semua tetangga dari node sekarang
        for tetangga in graf[node]:

            # Syarat tetangga diproses:
            # 1. tetangga masih satu komponen dengan node awal S
            # 2. tetangga belum pernah dikunjungi BFS
            if dalamKomponen[tetangga] == True and jarak[tetangga] == -1:

                # Jarak tetangga adalah jarak node sekarang + 1
                jarak[tetangga] = jarak[node] + 1

                # Masukkan tetangga ke antrian
                # supaya nanti tetangga tersebut ikut diproses
                antrian.append(tetangga)

    # Setelah BFS selesai,
    # jawabanNode adalah topik terjauh dari S
    # jawabanJarak adalah jaraknya
    return jawabanNode, jawabanJarak


def prosesKasus(n, m, s):
    # Fungsi ini memproses satu test case
    # graf[i] akan menyimpan semua tetangga dari node i
    graf = []

    # Buat list kosong sebanyak n + 1
    # Karena node dimulai dari 1 sampai n,
    # index 0 tidak dipakai
    for i in range(n + 1):
        graf.append([])

    # Membaca M edge / hubungan antar topik
    for i in range(m):
        u, v = map(int, input().split())

        # Karena hubungan bersifat dua arah,
        # maka u terhubung ke v dan v terhubung ke u
        graf[u].append(v)
        graf[v].append(u)

    # dalamKomponen[i] bernilai True jika node i
    # bisa dicapai dari node awal S
    dalamKomponen = [False] * (n + 1)

    # Langkah 1:
    # Gunakan DFS untuk mencari semua node
    # yang berada dalam satu komponen dengan S
    dfsKomponen(graf, s, dalamKomponen)

    # Langkah 2:
    # Gunakan BFS untuk mencari node dengan jarak terjauh dari S
    # BFS dipakai karena BFS menghasilkan jarak terpendek
    # dari S ke semua node yang bisa dijangkau
    node, jarak = bfsTerjauh(graf, s, dalamKomponen, n)

    # Cetak hasil:
    # node = topik yang paling jauh
    # jarak = jarak terpendek dari S ke node tersebut
    print(node, jarak)


# Membaca jumlah test case
t = int(input())

# Jalankan proses untuk setiap test case
for i in range(t):
    # n = jumlah topik / node
    # m = jumlah hubungan / edge
    # s = topik awal Dean
    n, m, s = map(int, input().split())

    # Proses satu kasus uji
    prosesKasus(n, m, s)