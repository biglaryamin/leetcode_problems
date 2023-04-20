def twoOutOfThree(nums1, nums2, nums3):
    counter = 0
    output_list = []

    for num in nums1:
        if num in nums2:
            counter += 1
        if num in nums3:
            counter += 1
        if counter >= 2:
            output_list.append(num)

        counter = 0

    return output_list



print(twoOutOfThree([1,1,3,2], [2,3], [3]))