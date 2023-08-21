import array #module array so we can have the apend and insert and pop functons

arr = array.array("i", [1,2,3]) # an array of integers and initialized

arr.append(4)
# arr.clear()
# arr.extend([1,2,3,5,4])
print(arr.__contains__(1))
arr = sorted(arr)

# loop over the array elements
for i in range(0, len(arr)):
    print(arr[i])