n = int(input())
sourceString = input()
targetString = input()
subString = ""
resultString = "Tentu saja bisa!"

indexAwal = 0
indexAkhir = 0
for i in range(n):
    if sourceString[i] != targetString[i]:
        indexAwal = i
        break

for i in range(n - 1, 0, -1):
    if sourceString[i] != targetString[i]:
        indexAkhir = i
        break

j = indexAkhir
for i in range(indexAwal, indexAkhir + 1):
    if sourceString[i] != targetString[j]:
        resultString = "Wah, tidak bisa :("
    j = j - 1

print(resultString)
