def twoSum(numbers, target):
    left, right = 0, len(numbers)-1

    while left < right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1,right+1]
        elif sum > target:
            right -= 1
        else:
            left += 1

    

def test_twoSum():
    assert (twoSum([2,7,11,15], 9) == [1,2])


test_twoSum()