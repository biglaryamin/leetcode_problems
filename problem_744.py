def nextGreatestLetter(letters, target):
    """Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
     Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'."""
    for letter in letters:
        if letter > target:
            return letter
    
    return list(letters)[0]



# binary search solution
# def nextGreatestLetter(nums, target):
#     nums.sort()
#     print(nums)
#     low = 0
#     high = len(nums)-1

#     while low < high:
#         mid = low + ((high-low) // 2)
        
#         if target > nums[mid]:
#             low = mid+1

#         elif target < nums[mid]:
#             high = mid

#         elif target == nums[mid]:
#             return mid
    
    # return "Not Found"

    
    


print(nextGreatestLetter([4,5,8,9,89,4,2,1,4,5,7,8,9,-45,0,0], 7))
