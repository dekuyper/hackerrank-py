n = 3
a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


def diagonalDifference(n, a):
    prim_sum = sec_sum = 0
    m = n - 1
    for i in range(n):
        j = m - i
        prim_sum += a[i][i]
        sec_sum += a[i][j]
    print(abs(prim_sum - sec_sum))

diagonalDifference(n, a)

