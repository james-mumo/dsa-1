nums = [2,2,3,4]

def dup(nums):
    h_set =  set()
    for i in nums:
        if i in h_set:
            return True
        h_set.add(i)
    return False

print(dup(nums))
