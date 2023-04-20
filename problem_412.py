def fizzBuzz(number):
    output = []

    end = number+1
    for num in range(1, end, 1):
        if num%15 == 0:
            output.append( "FizzBuzz")
        elif num%3 == 0:
            output.append("Fizz")
            continue
        elif num%5 == 0:
            output.append("Buzz")
        else:
            output.append(str(num))

    return output

print(fizzBuzz(15))