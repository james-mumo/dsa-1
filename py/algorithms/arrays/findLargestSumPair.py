def findLargestSumPair(arr):
    maxSum = -1
    for i in range(0, len(arr)-1):
        print(i)
        for j in range(i+1, len(arr)):
            sum = arr[j] + arr[i]
            if sum>maxSum:
                maxSum = sum
    return maxSum



def findLargestSumPair2(arr):
    n = len(arr)
    # init the initial largeset 1 and 2
    if arr[0] > arr[1]:
        f = arr[0]
        s = arr[1]
    else:
        f = arr[1]
        s = arr[0]

    # now we check the others
    for i in range(2, n):
        print(i)
        if arr[i] > f:
            s = f
            f = arr[i]
        elif arr[i]>s and arr[i]!=f:
            s = arr[i]

    return(f + s)



arr = [1,2,3,4,5,6]

print(findLargestSumPair(arr))
print(findLargestSumPair2(arr))