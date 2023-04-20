def reverseWords(input_string):
    """Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order."""
    output = ""
    words = input_string.split()
    for indx, word in enumerate(words):
        if indx == len(words)-1:
            output += word[::-1]
        else:
            output += word[::-1] + " "

    return output


assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"