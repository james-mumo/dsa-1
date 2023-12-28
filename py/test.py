# for loop

for i in range(33):
    if i == 32:
        break
    # print(i)

# linear time loop
arr = [1, 2, 4, 5, 6, ]

# for i in arr:
# print(i)


# nested Loop with n^2
arr1 = [[1, 2, 3], [5, 5, 6]]

for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        print(arr1[i][j])
