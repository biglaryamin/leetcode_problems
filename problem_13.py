def turn_roman_to_int(roman_number):
    dictionary = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    number = [dictionary.get(roman_number[0])]
    for i in range(1, len(roman_number)):
        if dictionary.get(roman_number[i]) > number[-1]:
            number[-1] = dictionary.get(roman_number[i]) - number[-1]
        else:
            number.append(dictionary.get(roman_number[i]))            
    return (sum(number))



def test_turn_roman_to_int():
    assert turn_roman_to_int("III")==3


test_turn_roman_to_int()