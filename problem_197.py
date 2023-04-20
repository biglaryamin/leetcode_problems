def twoSum(numbers, target):
    left = 0
    right = len(numbers)-1
    output = []

    while left <= right:
        if numbers[left]+numbers[right] > target:
            right -= 1
        elif numbers[left]+numbers[right] < target:
            left += 1
        else:
            output.append(left+1)
            output.append(right+1)
            return output




print(twoSum([-1, 0], -1))