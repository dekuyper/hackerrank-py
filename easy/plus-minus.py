n = 6
arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(n, arr):
    plus = 0.0
    minus = 0.0
    zero = 0.0
    for x in arr:
        if (x > 0):
            plus += 1.0
        if (x < 0):
            minus += 1.0
        if (x == 0):
            zero += 1.0

    return plus / n, minus / n, zero / n


pluses, minuses, zeroes = plusMinus(n, arr)

print pluses, "\n", minuses, "\n", zeroes
