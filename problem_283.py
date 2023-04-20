# Solution 1
def removeElement(nums, val):
    counter = 0
    pos = 0
    for indx, _ in enumerate(nums):
        if nums[indx] != val:
            nums[pos], nums[indx] = nums[indx], nums[pos]
            pos += 1
        else:
            counter += 1

    end_of_list = (len(nums)-1) - counter
    # print(counter)
    final_list = nums[:end_of_list+1]        
    return len(final_list) 



# Solution 2
def removeElement1(nums, val):
    while True:
        if val in nums:
            index_remove = nums.index(val)
            del nums[index_remove]
        else:
            break
    
    return len(nums)


nums = [0,1,2,2,3,0,4,2]
print(removeElement1(nums, 2))



