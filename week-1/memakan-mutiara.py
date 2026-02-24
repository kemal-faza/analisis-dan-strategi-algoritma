# Nama : Muhamad Kemal Faza
# NIM  : 24060124120013
# Lab  : E2
panjangTerowongan, sisaMeter, minimalMutiara = list(map(int, input().split()))
jumlahMutiara = 0

arr = list(map(int, input().split()))


for i in range(panjangTerowongan):

    while i > sisaMeter and jumlahMutiara > 0:
        jumlahMutiara -= 1
        sisaMeter += 7

    if i > sisaMeter:
        break

    if 1 <= arr[i] < 7:
        sisaMeter += arr[i]
    elif arr[i] == 7:
        jumlahMutiara += 1

if jumlahMutiara >= minimalMutiara:
    print(jumlahMutiara)
else:
    print(-1)

# N, Y, X = map(int, input().split())
# arr = list(map(int, input().split()))

# jangkauanMaksimal = Y - 1
# mutiaraSaatIni = 0

# rekorMutiara = 0

# for i in range(N):
#     while i > jangkauanMaksimal and mutiaraSaatIni > 0:
#         mutiaraSaatIni -= 1
#         jangkauanMaksimal += 7

#     if i > jangkauanMaksimal:
#         break

#     if 1 <= arr[i] <= 6:
#         jangkauanMaksimal += arr[i]
#     elif arr[i] == 7:
#         mutiaraSaatIni += 1
#         if mutiaraSaatIni > rekorMutiara:
#             rekorMutiara = mutiaraSaatIni

# if rekorMutiara >= X:
#     print(rekorMutiara)
# else:
#     print(-1)
