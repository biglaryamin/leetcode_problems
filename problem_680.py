# def validPalindrome(input_string:str) -> bool:
#     for indx, _ in enumerate(input_string):
#         temp_string = input_string
#         # delete the character at the index
#         temp_string = temp_string[:indx] + temp_string[indx+1:]

#         if temp_string == temp_string[::-1]:
#             return True
#     return False


# O(n) time | O(1) space
def validPalindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
        l += 1
        r -= 1
    return True




print(validPalindrome("abba"))