def ans1(arr):
    arr.sort(reverse=True)
    return arr[1]


def ans2(arr):
    largest = second = float('-inf')
    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif i > second and i != largest:
            second = i

    return second


arr = [33, 4, 2, 34, 12]
print(ans1(arr))
print(ans2(arr))
