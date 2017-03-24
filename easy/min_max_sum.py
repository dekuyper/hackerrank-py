arr = [1, 2, 3, 4, 5]
arr1 = [140638725, 436257910, 953274816, 734065819, 362748590]


def min_max_sum(arr):
    arr.sort()
    min_sum = sum(arr[:-1])
    max_sum = sum(arr[-4:])

    print min_sum, max_sum

min_max_sum(arr)
