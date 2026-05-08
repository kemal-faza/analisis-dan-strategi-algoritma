# Nama: Muhamad Kemal Faza
# NIM: 24060124120013
# Lab: E1


# Fungsi backtracking untuk mengecek kombinasi kotak permen
def backtrack(index, current_sum):
    # Jika jumlah sudah tepat sama dengan target
    if current_sum == T:
        return True
    # Jika sudah melewati semua kotak
    if index == N:
        return False
    # Pruning: jumlah sementara sudah melebihi target
    if current_sum > T:
        return False

    # Opsi 1: Ambil kotak ke-index
    if backtrack(index + 1, current_sum + listKotak[index]):
        return True
    # Opsi 2: Lewati kotak ke-index
    if backtrack(index + 1, current_sum):
        return True

    return False


# Baca input
N, T = map(int, input().split())
listKotak = list(map(int, input().split()))

# Cek kasus tidak memilih kotak (jumlah 0)
if T == 0:
    print("YES")
else:
    if backtrack(0, 0):
        print("YES")
    else:
        print("NO")
