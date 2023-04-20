def twoSum(nums, target):
    """Given an array of integers, return indices of the two numbers such that they add up to a specific target."""
    nums_len = len(nums)
    for i in range(nums_len):
        for j in range(i+1, nums_len):
            if nums[i] + nums[j] == target:
                return i,j


print(twoSum([3,2,4], 6))