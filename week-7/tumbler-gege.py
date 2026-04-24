n = int(input())
listPi = list(map(int, input().split()))


def dfs(node, visited, index):
    if node in visited:
        print(node + 1)
        return

    visited.add(index)
    if node not in visited:
        dfs(listPi[node] - 1, visited, node)
        return


for i in range(n):
    dfs(listPi[i] - 1, set(), i)
