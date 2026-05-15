# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab E1


def ambil_terkecil(open_list):
    minimum = 0

    for i in range(len(open_list)):
        if open_list[i][0] < open_list[minimum][0]:
            minimum = i

    return open_list.pop(minimum)


def greedy_bfs(graph, heuristik, awal, tujuan):
    open_list = [(heuristik[awal], awal, [awal])]
    visited = []
    checked = 0

    while open_list:
        _, node, rute = ambil_terkecil(open_list)
        checked += 1

        if node == tujuan:
            return rute, checked

        visited.append(node)

        for tetangga in graph[node]:
            if tetangga not in heuristik:
                continue

            if tetangga not in visited:
                sudah_di_open = False
                for _, n, _ in open_list:
                    if n == tetangga:
                        sudah_di_open = True
                        break

                if not sudah_di_open:
                    open_list.append((heuristik[tetangga], tetangga, rute + [tetangga]))

    return None, checked


N, M = map(int, input().split())

heuristik = {}
for _ in range(N):
    nama, h = input().split()
    heuristik[nama] = int(h)

graph = {nama: [] for nama in heuristik}

for _ in range(M):
    u, v = input().split()
    graph[u].append(v)

awal, tujuan = input().split()

rute, checked = greedy_bfs(graph, heuristik, awal, tujuan)

if rute:
    print(" -> ".join(rute))
else:
    print("TIDAK ADA")

print(f"DIPERIKSA: {checked}")
