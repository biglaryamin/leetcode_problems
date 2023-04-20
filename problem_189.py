def rotate(nums, k):
    repeat = 0
    while repeat<k:
        temp_number = nums[-1]
        del(nums[-1])
        nums.insert(0, temp_number)
        repeat += 1

    return nums


print(rotate([-1,-100,3,99], 2))