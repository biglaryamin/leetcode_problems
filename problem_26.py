def removeDuplicates(nums):
    j = 0
    i = 1

    while i < len(nums):
        if nums[i] == nums[j]:
            del nums[i]
        else:
            i += 1
            j += 1

    return nums


print(removeDuplicates([1,1,2]))