n, k = map(int, input().split())
listString = []
maxPoint = 0

for i in range(n):
    listString.append(list(map(str, input().split())))


def operasiString(number1, operator, number2):
    if operator == "*":
        return number1 * number2
    elif operator == "+":
        return number1 + number2


def max2(n1, n2):
    return n1 if n1 > n2 else n2


def hitungPoint(currentPoint, index):
    global maxPoint
    if index == n:
        return currentPoint

    temp1 = (
        hitungPoint(
            operasiString(
                currentPoint, listString[index][0], int(listString[index][1])
            ),
            index + 1,
        )
        or 0
    )
    temp2 = (
        hitungPoint(
            operasiString(
                currentPoint, listString[index][2], int(listString[index][3])
            ),
            index + 1,
        )
        or 0
    )

    return max2(temp1, temp2)


print(hitungPoint(k, 0))
