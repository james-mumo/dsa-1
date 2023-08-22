def firstRep(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                return i

    return -1


def mostRep(arr):
    Min = -1
    myDict = dict()
    for i in range(len(arr)-1, 0, -1):
        if arr[i] in myDict.keys():
            Min = i
        else:
            myDict[arr[i]] = 1
    return arr[Min]





arr = [1, 2, 13, 1, 10, 34, 13, 14, 23, 10, 10, 10]
print(mostRep(arr))
print(firstRep(arr))

