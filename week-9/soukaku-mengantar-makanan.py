n = int(input())
jarak = []
for _ in range(n):
    jarak.append(list(map(int, input().split())))
awal = 0


def hitung_bound(visited, biaya_sekarang):
    bound = biaya_sekarang
    for i in range(n):
        if not visited[i]:
            minimum = float("inf")
            for j in range(n):
                if i != j and jarak[i][j] < minimum:
                    minimum = jarak[i][j]
            bound += minimum
    return bound


def tsp_branch_bound():
    solusi_terbaik = [float("inf")]
    rute_terbaik = [[]]

    visited = [False] * n
    visited[awal] = True

    def dfs(posisi, visited, rute, biaya):
        if len(rute) == n:
            total = biaya + jarak[posisi][awal]
            if total < solusi_terbaik[0]:
                solusi_terbaik[0] = total
                rute_terbaik[0] = rute + [awal]
            return

        for i in range(n):
            if not visited[i]:
                biaya_baru = biaya + jarak[posisi][i]
                bound = hitung_bound(visited, biaya_baru)

                if bound < solusi_terbaik[0]:
                    visited[i] = True
                    dfs(i, visited, rute + [i], biaya_baru)
                    visited[i] = False

    dfs(awal, visited, [awal], 0)
    return solusi_terbaik[0]


print(tsp_branch_bound())
