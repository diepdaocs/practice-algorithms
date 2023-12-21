def binary_search(a, n):
    i, j = 0, len(a) - 1
    while i <= j:
        mid = int((i + j) / 2)
        if a[mid] == n:
            return mid
        elif a[mid] > n:
            mid -= 1
            j = mid
        else:
            mid += 1
            i = mid

    return -1


def binary_search_recursive(a, n):
    return binary_search_rec(a, n, 0, len(a) - 1)


def binary_search_rec(a, n, i, j):
    if i > j:
        return -1

    mid = int((i + j) / 2)
    if n < a[mid]:
        return binary_search_rec(a, n, i, mid - 1)
    elif n > a[mid]:
        return binary_search_rec(a, n, mid + 1, j)
    else:
        return mid


def main():
    a = [1, 2, 4, 8, 10, 15, 20]
    assert binary_search(a, 8) == 3
    assert binary_search(a, 2) == 1
    assert binary_search(a, 1) == 0
    assert binary_search(a, 20) == 6
    assert binary_search(a, 21) == -1

    assert binary_search_recursive(a, 8) == 3
    assert binary_search_recursive(a, 2) == 1, binary_search_recursive(a, 2)
    assert binary_search_recursive(a, 1) == 0
    assert binary_search_recursive(a, 20) == 6
    assert binary_search_recursive(a, 21) == -1


if __name__ == '__main__':
    main()
