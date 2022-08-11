def num_parse(number, divisor):
    output = number % divisor
    return output
    
def user_input():
    number = input("Please enter a number: ")
    divisor = input("Please enter a divisor: ")
    
    try:
        number = int(number)
        divisor = int(divisor)
    except ValueError:
        print("Invalid input...exiting")
        exit()
    
    if num_parse(number, 2) == 0:
        print("The number you entered is even.")
        if num_parse(number, 4) == 0:
            print("It looks like the number you entered is a multiple of four.")
        else:
            pass
        if num_parse(number, divisor) == 0:
            print("It looks like the number you entered is a multiple of your divisor, " + str(divisor) + ".")
        else:
            pass
    elif num_parse(number, 2) != 0:
        print("The number you entered is not even.")
        if num_parse(number, divisor) == 0:
            print("It looks like the number you entered is a multiple of your divisor, " + str(divisor) + ".")
        else:
            pass
        
user_input()