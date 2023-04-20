def permute(nums):
    # output is every permutation of nums
    output = []
    # if nums is empty, return empty list
    if len(nums) == 0:
        return output
    # if nums has one element, return that element
    if len(nums) == 1:
        return [nums]   
    # for each element in nums
    for i in range(len(nums)):
        # get the element
        n = nums[i]
        # get the remaining elements
        remaining = nums[:i] + nums[i+1:]
        # for each permutation of the remaining elements
        for p in permute(remaining):
            # add the current element to the front of the permutation
            output.append([n] + p)

    return output


print(permute([1,2,3]))