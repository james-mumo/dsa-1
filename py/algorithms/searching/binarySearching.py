# must be sorted
# acces is 

arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23


def itBinSearch(arr, target):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


print(itBinSearch(arr, target))


def recBinSearch(arr, key, l, r):
    while l <= r:
        mid = l + (r - l) // 2

        # if found return it
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return recBinSearch(arr, key, mid + 1, r)
        else:
            return recBinSearch(arr, key, 0, mid - 1)
    return -1


rec_arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 72
print(recBinSearch(rec_arr, key, 0, len(rec_arr) - 1))
