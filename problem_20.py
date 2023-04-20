def isValid(input_string):
    """Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid."""
    paranthese_dict = {'(': ')', '{': '}', '[': ']'}

    # res_dct = {input_string[i]: input_string[i + 1] for i in range(0, len(input_string), 2)}

    # for char in res_dct:
    #     if res_dct[char] == paranthese_dict[char]:
    #         pass
    #     else:
    #         return False
    
    # return True

    input_string = list(input_string)
    while True:
        if input_string:    
            the_char = input_string[0]    
            temp_string = input_string[1:]

            if paranthese_dict[the_char] in input_string[1:]:
                temp_indx = input_string[1:].index(the_char)
                del(temp_string[temp_indx])

            else:
                return False
                    
        else:
            return True


            
print(isValid("()"))