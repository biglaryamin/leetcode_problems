def reverseString(input_string):
    left, right = 0, len(input_string)-1

    while left < right:
        input_string[left], input_string[right] = input_string[right], input_string[left]
        left += 1
        right -= 1
    return input_string



print(reverseString(["h","e","l","l","o"]))