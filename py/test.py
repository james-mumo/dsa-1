def TwoSum(nums, target):
    visited = {}
    for k, v in enumerate(nums):
        diff = target - v
        if diff in visited:
            return [visited[diff], k]
        visited[v] = k
    return


nums = [2, 7, 11, 15]
target = 9

print(TwoSum(nums, target))