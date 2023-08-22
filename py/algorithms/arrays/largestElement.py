# largest 3 elements
import sys

def largestThree(arr, arr_size):
    if arr_size < 3:
        print("Invalid Array")
        return

    f = s = t = -sys.maxsize

    for i in range(0, arr_size):
        if arr[i] > f:
            t = s
            s = f
            f = arr[i]

        elif arr[i] > s:
            t = s
            s = arr[i]

        else:
            t = arr[i]

    print("Largest 3 are :", f, s, t)


arr = [12, 13, 1, 10, 34, 1]
n = len(arr)
largestThree(arr, n)