# def containsNearbyDuplicate(nums, k):
#     left, right = 0, 1
#     while left < len(nums)-1:
#         if right <= len(nums)-1 and right-left <= k:
#             if nums[left] == nums[right]:
#                 if right - left <= k:
#                     return True
#                 else:
#                     right += 1
#             else:
#                 right += 1
#         else:
#             left += 1
#             right = left+1
    
#     return False



# print(containsNearbyDuplicate([1,0,1,1], 1))


def containsNearbyDuplicate(nums, k):
    """Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k."""
    d = {}
    for i, num in enumerate(nums):
        if num in d and i - d[num] <= k:
            return True
        d[num] = i
    return False



print(containsNearbyDuplicate([1,0,1,1], 1))
