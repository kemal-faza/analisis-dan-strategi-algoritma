n, m, s = map(int, input().split())
listPath = []

for i in range(m):
    listPath.append(list(map(int, input().split())))


def dfs(node, visited):
    if node == s:
        return True

    visited.add(node)
    for neighbor in listPath:
        if neighbor[0] == node:
            if neighbor[1] == s:
                return True
            elif neighbor[1] not in visited and dfs(neighbor[1], visited):
                return True
    return False


isCanReturn = False
for neighbor in listPath:
    if neighbor[0] == s and dfs(neighbor[1], {neighbor[0]}):
        isCanReturn = True
        break

print("YES") if isCanReturn else print("NO")
