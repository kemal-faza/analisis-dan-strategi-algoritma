from math import sqrt


def codeBlue(ranks, clue):
    l, r = 0, max(ranks) * clue**2
    ans = 0

    while l < r:
        mid = (l + r) // 2
        jum = 0

        for rank in ranks:
            jum += int(sqrt(mid / rank))

        if jum >= clue:
            # ans = mid
            # r = mid - 1
            r = mid
        else:
            l = mid + 1

        if jum == clue:
            ans = mid

    return ans


clue = int(input())
ranks = list(map(int, input().split()))

print(codeBlue(ranks, clue))
