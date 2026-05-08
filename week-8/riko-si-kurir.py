# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1


import heapq


# Fungsi Dijkstra untuk mencari biaya termurah dari start ke semua kota
def dijkstra(graph, start):
    # graph: dict {node: [(tetangga, bobot), ...]}
    # Inisialisasi jarak semua node dengan tak hingga
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    # Priority queue (min-heap) berisi (jarak, node)
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Jika jarak saat ini lebih besar dari jarak tersimpan, lewati
        if current_distance > distances[current_node]:
            continue

        # Eksplorasi tetangga dari node saat ini
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


# Baca input
N, M = map(int, input().split())

# Inisialisasi graf (adjacency list)
graph = {i: [] for i in range(1, N + 1)}

# Baca jalan dua arah
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # Karena jalan dapat dilalui dua arah

# Baca kota asal dan tujuan
S, T = map(int, input().split())

# Jalankan Dijkstra dari kota S
distances = dijkstra(graph, S)

# Cek apakah kota T dapat dicapai
if distances[T] == float("inf"):
    print(-1)
else:
    print(distances[T])
