# must be sorted
# acces is 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

def itBinSearch(arr, target):
    l = 0
    r = len(arr)-1

    while l<=r:
        mid = l + (r-l)//2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1 
    return -1

print(itBinSearch(arr, target))


def itBin(arr, t):
    l = 0
    r = len(arr)-1
    
    while l<=r:
        mid = l + (r - l)//2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            l = mid + 1
        else:
            r = mid -1
    return -1
    
arrayF = [1,2,34,5,6,3]
sortedF =  sorted(arrayF)

print(itBin(sortedF, 3))