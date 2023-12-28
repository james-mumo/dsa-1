nums = [2, 2, 3, 4]


def dups(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False


print(dups(nums))