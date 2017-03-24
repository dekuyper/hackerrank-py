# Sum of large inputs
N = 5
arr = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]


def printSumOfElementsInList(arr):
    sum = 0
    for x in arr:
        sum += x
    print(sum)

printSumOfElementsInList(arr)
