def sortedSquares(numbers):
    """Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order."""
    return sorted([num*num for num in numbers])




print(sortedSquares([-4,-1,0,3,10]))
