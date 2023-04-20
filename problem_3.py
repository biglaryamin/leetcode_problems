def lengthOfLongestSubstring(input_string) -> int:

    repeat_list= []
    max_sub = 0
    
    for idx, char in enumerate(input_string):
        if char in repeat_list:
            # max_sub = max(max_sub, len(repeat_list))
            del(repeat_list[0])
            while char in repeat_list:
                del(repeat_list[0])
            repeat_list.append(char)
        else:
            repeat_list.append(char)
            max_sub = max(max_sub, len(repeat_list))

    return max_sub


def test_lengthOfLongestSubstring():
    assert lengthOfLongestSubstring("pwwkew") == 3


test_lengthOfLongestSubstring()