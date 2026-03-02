n = int(input())

usedCol = [False] * n
usedDiagMain = [False] * (2 * n - 1)
usedDiagSecondary = [False] * (2 * n - 1)
queenColInRow = [-1] * n


def placeQueen(row):
    if row == n:
        return True

    for col in range(n):
        diagMain = row - col + (n - 1)
        diagSecondary = row + col

        if usedCol[col] or usedDiagMain[diagMain] or usedDiagSecondary[diagSecondary]:
            continue

        usedCol[col] = True
        usedDiagMain[diagMain] = True
        usedDiagSecondary[diagSecondary] = True
        queenColInRow[row] = col

        if placeQueen(row + 1):
            return True

        usedCol[col] = False
        usedDiagMain[diagMain] = False
        usedDiagSecondary[diagSecondary] = False
        queenColInRow[row] = -1

    return False


if placeQueen(0):
    for row in range(n):
        boardRow = ["."] * n
        boardRow[queenColInRow[row]] = "Q"
        print("".join(boardRow))
else:
    print("Kerajaan tidak dapat dilindungi!")
