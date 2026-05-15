# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab E1


def ambil_terkecil(open_list):
    minimum = 0

    for i in range(len(open_list)):
        h_i, node_i, _ = open_list[i]
        h_min, node_min, _ = open_list[minimum]

        if h_i < h_min or (h_i == h_min and node_i < node_min):
            minimum = i

    return open_list.pop(minimum)


def greedy_bfs(graph, h, awal, tujuan):
    open_list = [(h[awal], awal, [awal])]
    visited = []
    expanded = []

    while open_list:
        _, node, rute = ambil_terkecil(open_list)
        expanded.append(node)

        if node == tujuan:
            return rute, expanded

        visited.append(node)

        for tetangga, _ in graph[node]:
            if tetangga not in visited:
                sudah_di_open = False
                for _, n, _ in open_list:
                    if n == tetangga:
                        sudah_di_open = True
                        break

                if not sudah_di_open:
                    open_list.append((h[tetangga], tetangga, rute + [tetangga]))

    return None, expanded


def hitung_biaya(graph, rute):
    total = 0
    for i in range(len(rute) - 1):
        u = rute[i]
        v = rute[i + 1]
        for tetangga, w in graph[u]:
            if tetangga == v:
                total += w
                break
    return total


N, M = map(int, input().split())
S, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

semua_baris = []
try:
    while True:
        baris = input().strip()
        semua_baris.append(baris)
except EOFError:
    pass

nilai_h = list(map(int, semua_baris[-1].split()))

for baris in semua_baris[:-1]:
    u, v, w = map(int, baris.split())
    graph[u].append((v, w))

h = [0] * (N + 1)
for i in range(1, N + 1):
    h[i] = nilai_h[i - 1]

rute, expanded = greedy_bfs(graph, h, S, E)

cost = hitung_biaya(graph, rute)

print("Path:", " ".join(map(str, rute)))
print("Cost:", cost)
print("Expanded:", " ".join(map(str, expanded)))
