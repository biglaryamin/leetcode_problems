def majorityElement(nums):
    repeat_dict = {}
    for num in nums:
        if num in repeat_dict:
            repeat_dict[num] += 1
        else:
            repeat_dict[num] = 1


    for number, repeat in repeat_dict.items():
        if repeat > len(nums)/2:
            return number




print(majorityElement([2,2,1,1,1,2,2]))