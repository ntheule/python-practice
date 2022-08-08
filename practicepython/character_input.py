from datetime import date
import os
from xml.etree.ElementTree import tostring

def char_input():
    # Ask user for input
    name = input("Please enter your name: ")
    age = input("Please enter your age: ")
    RepeatNumber = int(input("Please enter a number: "))

    # Loop over provided number to repeat previous message
    while RepeatNumber > 0:
        print("Please enter a number: ")
        RepeatNumber -= 1

    # Find the current year and set the result age
    year = date.today().year
    ResultAge = 100

    # Calculate the year the user will turn ResultAge
    YearFinal = year + (ResultAge - int(age))
    
    result = "Hello " + name + ". You will turn " + str(ResultAge) + " years old in the year " + str(YearFinal) + "."

    # Print result
    # print("Hello " + name + ". You will turn " + str(ResultAge) + " years old in the year " + str(YearFinal) + ".")