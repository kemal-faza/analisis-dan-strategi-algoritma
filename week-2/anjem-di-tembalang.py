# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2
n = int(input())
matriksJarak = []
for i in range(n):
    matriksJarak.append(list(map(int, input().split())))
baseChar = "A"
jarakMinimal = float("inf")
ruteTerbaik = []


def exploreMatrix(currentNode, totalJarak, jumlahDikunjungi, visited, path):
    global jarakMinimal, ruteTerbaik

    if totalJarak >= jarakMinimal:
        return

    if jumlahDikunjungi == n:
        totalJarak += matriksJarak[currentNode][0]
        if totalJarak < jarakMinimal:
            jarakMinimal = totalJarak
            ruteTerbaik = path[:] + [0]
        return

    for nextNode in range(1, n):
        if not visited[nextNode]:
            visited[nextNode] = True
            path.append(nextNode)
            exploreMatrix(
                nextNode,
                totalJarak + matriksJarak[currentNode][nextNode],
                jumlahDikunjungi + 1,
                visited,
                path,
            )
            path.pop()
            visited[nextNode] = False


visited = [False] * n
visited[0] = True
exploreMatrix(0, 0, 1, visited, [0])

print(jarakMinimal)

hasilRute = []
for index in ruteTerbaik:
    hasilRute.append(chr(ord(baseChar) + index))
print(" ".join(hasilRute))
