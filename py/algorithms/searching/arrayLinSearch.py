
# searcing an array in py

def search(ar, key):
    for i in ar:
        if i == key:
            return ar.index(i)
    return -1

ar = [1,2,3,4,5,6,7,8,9]
key = 5
print(search(ar, key))


def search2(arr, key):
    for i in range(0, len(arr)):
        if arr[i] == key:
            return i
    return -1

print(search(ar, key))