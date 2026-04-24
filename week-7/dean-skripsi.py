t = int(input())

listNMS = []
listPathTopik = []
for i in range(t):
    listNMS.append(list(map(int, input().split())))
    pathTopik = []
    for j in range(listNMS[i][1]):
        pathTopik.append(list(map(int, input().split())))
    listPathTopik.append(pathTopik)

def dfs(indeks, visited, maxLangkah):
    if 

for i in range(len(listNMS)):
    n, m, s = listNMS[0], listNMS[1], listNMS[2]
    for j in range(n):
        maxLangkah = 0
        dfs(j, set(), maxLangkah)


