# in 3 parts mid1 and mid2

import math as mt
def tSearch(arr, key, l, r):
   
    while l<r:
        # mid 1 and 2
        mid1 = l + (r - l)//3
        mid2 = r - (r - l)//3
        # print(mid1, mid2)
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2

        if key < arr[mid1]:
            return tSearch(arr, key, l, mid1 - 1)
        elif key > arr[mid2]:
            return tSearch(arr, key, mid2 + 1, r)
        else:
            return tSearch(arr, key, mid1+1, mid2-1)

    return -1

arr = [1,2,3,4,5,6,7,8,9]
key = 5



print(tSearch(arr, key, 0, len(arr)-1))


        

