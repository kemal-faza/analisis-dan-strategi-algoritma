n = int(input())
biaya = []
for _ in range(n):
    baris = list(map(int, input().split()))
    biaya.append(baris)


def hitung_bound(level, biaya_sekarang, tugas_terpakai):
    bound = biaya_sekarang
    for i in range(level, n):
        minimum = float("inf")
        for j in range(n):
            if not tugas_terpakai[j] and biaya[i][j] < minimum:
                minimum = biaya[i][j]
        bound += minimum
    return bound


def assignment_branch_bound():
    solusi_terbaik = [float("inf")]

    tugas_terpakai = [False] * n

    def dfs(level, tugas_terpakai, biaya_sekarang):
        if level == n:
            if biaya_sekarang < solusi_terbaik[0]:
                solusi_terbaik[0] = biaya_sekarang
            return

        for j in range(n):
            if not tugas_terpakai[j]:
                biaya_baru = biaya_sekarang + biaya[level][j]
                bound = hitung_bound(level + 1, biaya_baru, tugas_terpakai)

                if bound < solusi_terbaik[0]:
                    tugas_terpakai[j] = True
                    dfs(level + 1, tugas_terpakai, biaya_baru)
                    tugas_terpakai[j] = False

    dfs(0, tugas_terpakai, 0)
    return solusi_terbaik[0]


print(assignment_branch_bound())
