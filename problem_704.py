def search(nums, target):
    """Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity."""
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = left + ((right-left)//2)

        if target < nums[mid]:
            right = mid
        elif target > nums[mid]:
            left = mid+1
        else:
            return mid

    return -1


print(search([-1,0,3,5,9,12], 9))