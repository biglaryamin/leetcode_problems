# def singleNumber(nums) -> int:
#     nums_dict = {}

#     for num in nums:
#         nums_dict[num] = nums.count(num)

#     for num, rep in nums_dict.items():
#         if rep == 1:
#             return num


# print(singleNumber([2,2,1]))




def singleNumber(nums) -> int:
    nums_dict = {}

    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
        else:
            nums_dict[num] = 1
    
    for num, rep in nums_dict.items():
        if rep == 1:
            return num


print(singleNumber([4,1,2,1,2]))