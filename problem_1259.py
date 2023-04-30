def findNumbers(nums):
    res = 0
    for num in nums:
        count = 0
        for _ in str(num):
            count += 1
        if count%2 == 0:
            res += 1

    return res


print(findNumbers([555,901,482,1771]))