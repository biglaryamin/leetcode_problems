def addDigits(num):
    """Given a non-negative integer num, repeatedly add all its digits until the result has only one digit."""
    while num > 9:
        num = sum([int(i) for i in str(num)])

    return num


# def addDigits(num):
#     sum = 0
#     while num > 0:
#         sum = sum + num%10
#         num = num//10
#     if sum > 9:
#         return addDigits(sum)

#     return sum


print(addDigits(0))