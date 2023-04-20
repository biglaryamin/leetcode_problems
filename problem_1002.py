from collections import Counter

def commonChars(words_list):
    overall = []
    output = []

    for indx, _ in enumerate(words_list):
        words_list[indx] = list(set(words_list[indx]))
        overall += "".join(words_list[indx])


    n = len(words_list)
    # return dict(Counter(overall))
    char_dict = dict(Counter(overall))
    for char in char_dict:
        if char_dict[char] == 3:
            output.append(char)

    return output

print(commonChars(["bella","label","roller"]))