# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1


import heapq


# Fungsi A* untuk mencari biaya minimum dari start ke goal
def a_star(start, goal, graph, h):
    # h: list nilai heuristik (indeks 1-based)
    open_set = []
    # Push node awal: (f_score, g_score, node), f = g + h = 0 + h[start]
    heapq.heappush(open_set, (h[start], 0, start))
    g_score = {start: 0}

    while open_set:
        _, current_g, current = heapq.heappop(open_set)

        # Jika sudah sampai tujuan, kembalikan biaya yang ditempuh
        if current == goal:
            return current_g

        # Lewati jika g saat ini lebih besar dari yang tersimpan
        if current_g > g_score.get(current, float("inf")):
            continue

        # Eksplorasi tetangga
        for neighbor, weight in graph[current]:
            tentative_g = current_g + weight

            # Jika jalur baru ke tetangga lebih baik
            if tentative_g < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h[neighbor]
                heapq.heappush(open_set, (f_score, tentative_g, neighbor))

    # Tujuan tidak dapat dicapai
    return -1


# Baca input
N, M = map(int, input().split())

# Baca nilai heuristik (1-based, index 0 sebagai dummy)
h = [0]
h.extend(map(int, input().split()))

# Inisialisasi graf (adjacency list)
graph = {i: [] for i in range(1, N + 1)}

# Baca koridor dua arah
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

# Baca ruang awal dan tujuan
S, T = map(int, input().split())

# Jalankan A*
result = a_star(S, T, graph, h)

# Cetak hasil
print(result)
