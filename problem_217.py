def containsDuplicate(nums):
    repeated_nums_dict = {}
    for num in nums:
        if num in repeated_nums_dict:
            return True 
        else:
            repeated_nums_dict[num] = 1

    return False


print(containsDuplicate([1,2,3,4]))