def isValid(phrase) -> bool:
    stack = []
    mp = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    for char in phrase:
        if char in mp and len(stack) > 0:
            last_val = stack.pop()            
            if mp[char] != last_val:
                return False
        else:
            stack.append(char)
    
    return not stack


def test_is_valid_parentheses():
    assert isValid("{}[]{}")==True


test_is_valid_parentheses()