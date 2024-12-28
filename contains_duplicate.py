'''
Given an integer array nums and an integer k, 
return true if there are two distinct indices i and j in the 
array such that nums[i] == nums[j] and abs(i - j) <= k.
'''

def contains_nearby_duplicate(nums, k):
    seen = {}
    for i, num, in enumerate(nums):
        if num in seen and abs(i - seen[num]) <= k:
            return True
        seen[num] = i
    return False


print(contains_nearby_duplicate([1,2,3,1], 3))
print(contains_nearby_duplicate([1,2,3,1,2,3], 2))
