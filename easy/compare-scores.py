# My Code

A = [5, 6, 7, 11]
B = [3, 6, 10, 10]


def printScores(a, b):
    score_a = score_b = 0
    for idx, number in enumerate(a):
        if number > b[idx]:
            score_a += 1
        if number < b[idx]:
            score_b += 1
    print(str(score_a) + ' ' + str(score_b))


printScores(A, B)

