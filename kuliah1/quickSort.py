def quickSort(array, low, high):
    if low < high:
        mid = partisi(array, low, high)
        quickSort(array, low, mid)
        quickSort(array, mid + 1, high)


def partisi(array, low, high):
    pivot = array[(low + high) // 2]
    p = low
    q = high

    while True:

        while array[p] < pivot:
            p += 1

        while array[q] > pivot:
            q -= 1

        print(f"{array=}, {array[p]=}, {p=}, {array[q]=}, {q=}")

        if p >= q:
            return q
        else:
            temp = array[p]
            array[p] = array[q]
            array[q] = temp

            p += 1
            q -= 1


listAngka = list(map(int, input().split()))
quickSort(listAngka, 0, len(listAngka) - 1)
print(f"{listAngka=}")
