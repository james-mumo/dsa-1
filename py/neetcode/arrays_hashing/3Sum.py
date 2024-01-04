# def ThreeSum(A, arr_size, sum):
def tsum(nums, key):
    res = []
    nums.sort()

    for k, v in enumerate(nums):
        if k > 0 and v == nums[v - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a +
