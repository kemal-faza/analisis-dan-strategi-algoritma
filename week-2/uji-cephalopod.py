# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2
teks = input()


def searchXY(teksXY, countXY):
    if len(teksXY) < 2 and countXY == 0:
        print(False)
        return
    subTeks = teksXY[0:2]
    if subTeks == "XY":
        countXY += 1
    if len(teksXY) == 1:
        print(countXY % 2 == 0)
        return
    searchXY(teksXY[1:], countXY)


searchXY(teks, 0)
