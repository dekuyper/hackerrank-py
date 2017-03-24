def staircase(n):
    matrix = ''
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if(j > (n - i)):
                matrix += '#'
                continue
            matrix += " "
        matrix += "\n"
    print matrix

