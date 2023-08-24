def isArraySorted(arr, n):
    if (n == 1 or n == 0):
        return True
    else:
        for i in range(1, n):
            if (arr[i - 1] > arr[i]):
                return False
        return True


print(isArraySorted([1,2,3,4,5,6], 6))