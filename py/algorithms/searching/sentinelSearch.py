def search(arr, target):
    last_element = arr[len(arr)-1]
    arr[len(arr)-1] = target

    i = 0

    while arr[i] != target:
        i+=1

    arr[len(arr)-1] = last_element

    if i < len(arr)-1 or arr[len(arr)-1]==target:
        return i
    else:
        return -1


arr = [3,53,4,33,4,5,66,7]
target = 36

print(search(arr, target))
