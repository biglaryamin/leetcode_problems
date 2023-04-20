def calculate_sum(number):
    sum = 0
    for i in range(len(str(number))):
        sum += (number%10)*(number%10) 
        number = number//10

    return sum



def isHappy(main_number):
    counter = 0
    num = main_number

    while True:
        temp_number = calculate_sum(num)
        num = temp_number

        if temp_number == 1:
            return True

        if counter == 100:
            return False
        
        counter += 1



print(isHappy(20))