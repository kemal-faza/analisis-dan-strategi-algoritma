# def pangkat2(x, y):
#     hasil = 1
#     for i in range(x, y):
#         hasil *= x
#     return hasil


# print(pangkat2(2, 100000))


def pangkat3(x, y, z):
    hasil = 1
    for i in range(x, y):
        for j in range(x, z):
            hasil *= x * z
    return hasil


print(pangkat3(2, 100, 100))
