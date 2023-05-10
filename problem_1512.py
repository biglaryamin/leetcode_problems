def numIdenticalPairs(nums):
    counter = 0

    for indx1, x in enumerate(nums):
        for indx2, y in enumerate(nums):
            if indx1 == indx2:
                continue
            if x == y and indx1 < indx2:
                counter += 1


    return counter