# # # DAY -1
# # print("Hello World")

# # # WAP To show the output as provided!

# # print('what to print')

# # # Use of nextline Characters

# # print("Hi !!\n How \tare \byou !!How\f is\r everything\t going\v? ")

# # # String Concatenation
# # print("hello" + "Vibhor")

# # # Finishing String Concatenation
# # print("hello" + " " + "Vibhor")

# # # P-2
# # print("DAY 1 -  STRING MAIPULATION")
# # print("String Concatenation is fone with the "+" " + "sign.")
# # print ("e.g print(" + "Hello" + " "  +"world)")
# # print("New lines can be created with a \n Hurray")

# # # input the  data
# # # input("What is your name?\n")

# # # P-3

# # # name = input("What is your name?\n")
# # # print(len(name))

# # # Variables
# # name= "Vibhor"
# # print(name)

# # # P=4
# # # SWAP the values of the variables a and b using user input

# # # take two varaibles a znd B
# # # we take another variable c
# # # store the values of let us say b into c and then intert=change the valuyes
# # # finally store The value of c to the the remaining variable

# # # a = input("Inpout The value of a=")
# # # b = input("Inpout The value of b=")
# # # c = a
# # # a = b
# # # b = c
# # # print("the value of a : "+ a + "\n" + "the value of b : "+ b)

# # # Data Types
# # # Int ,  String  ,Float , Boolean
# # # print("Hello"[4])
# # # print("123"+"456")

# # # # Fix Type Error
# # # num_char = len(input("What is your name?\n"))
# # # # print("Your name has " + num_char + "characters.")
# # # print(type(num_char))
# # # # Type Casting

# # # print("Your name has " + str(num_char) + " characters.")
# # print(70 + float(100.5))
# # print(str(70) + str(100.5))

# # # P5
# # # WAP that adds digits in a 2 digit number . If the input was 24 , the output should be 6

# # # a  = input("Enter the first number a: ")
# # # first_digit = a[0]
# # # second_digit = a[1]
# # # result = int(first_digit)+ int(second_digit)
# # # print("the value of "+ str(result))

# # # PEMDAS equalivlent to BODMAS in Maths
# # # PS-6
# # # Calculate The BMI
# # # height = input("Enter your height in m: ")
# # # weight = input("Enter your weight in kg: ")

# # # bmi = int(weight) / float(height) ** 2
# # # print("bmi is: " + str(bmi) )

# # # Number Manipulation and F Strings
# # print(int(8/3))

# # print(round(8/3,8))

# # print(type(8 // 3))

# # # String Inetrpolation use {} in the String with using f""eg . f" foo {value}"

# # # Control Statements

# # # print("Welcome to Code")
# # # height = int(input("What is your height in cm : "))
# # # if height > 120 :
# # #     print("you can ride")
# # # else:
# # #   print("you cannot ride")

# # # #  Code Challenge
# # # # ODD or EVEN

# # # odd_or_even = int(input("Enter any number : "))
# # # if odd_or_even % 2 == 0 :
# # #   print(f"Number {odd_or_even} is even")
# # # else:
# # #   print(f"Number {odd_or_even} is odd")

# # # BMI Excercise 2
# # # height = float (input("enter your height in meters : "))
# # # weight = float (input("enter your weight in kilograms : "))
# # # bmi = round(weight/height ** 2)
# # # if bmi < 18.5 :
# # #   print(f"Your bmi is {bmi} and you are underweight.")
# # # elif bmi < 25:
# # #   print(f"Your bmi is {bmi} and you are normal weight.")
# # # elif bmi < 30  :
# # #    print(f"Your bmi is {bmi} and you are over weight.")
# # # elif bmi < 35 :
# # #    print(f"Your bmi is {bmi} and you are obese.")
# # # else :
# # #    print(f"Your bmi is {bmi} and you are clinically obese.")

# # # Leap Year
# # # Condition
# # # year  % 4 == 0
# # # year is not divisible by 100 unless it % 400 = 0
# # # year = int(input("Enter the year : "))
# # # if year % 4 == 0 :
# # #   if year % 100 == 0 :
# # #     if year %  400 == 0:
# # #         print("It is  a leap year")
# # #     else:
# # #       print("It is not a leap year")
# # #   else:
# # #     print("It is not a leap year")
# # # else:
# # #   print("It is not a leap year")

# # # Pizza Order Excercise

# # # print("Welcome to Python Pizza Delivery")
# # # size = input("What size pizza do you want? S ,M , L")
# # # add_peparoni = input("Do you want peparoni? Y or N")
# # # add_extra_cheese = input("Do you want extra_cheese? Y or N")

# # #Randomization
# # import random

# # random_integer = random.randint(1,10)
# # print(f"random number between 1 and 10 is {random_integer}")

# # random_float = random.uniform(1,5)
# # print(f"random float number between 1 and 5 is {random_float}")

# # #Head or Tail  Game
# # head_or_tail = random.randint(0,1)
# # if  head_or_tail == 1:
# #   print("Tails")
# # else:
# #   print("Head")

# # # Collections
# # # Lists
# # # states_of_india = ["Haryana","Maharashtra","Punjab","Uttar Pradesh"]
# # # print(states_of_india[2])
# # # states_of_india.extend(["Odhisha"])
# # # print(states_of_india)

# # # # P-8
# # # # Split the String Method
# # # names_string = input("Give me everybody's names. separated by a comma")
# # # names = names_string.split(", ")

# # # DAY - 10
# # # Day10
# # # Calculator

# # from  calculator import simple_function

# # print(simple_function())

# # from name_format import format_name

# # format_name("viBHor","GUPTA")

# # Leap year using Function

# from leap_year_using_functions import isLeapYear

# print(isLeapYear(2000))






# # DAY 5 
# fruits = ["Apple","Orange","Pear"]
# for fruit in fruits:
#   print(fruit)
#   print(fruits)


# # Problem Set 5-A


# # # WAP to calculate the average heioght from the lists of height
# # students_height = input("Input a list of student heights").split()
# # for n in range(0, len(students_height)):
# #     students_height[n] = int(students_height[n])
# # print(students_height)

# # # Cannot use len and sun function 
# # Don't use len() and sum()
# # Here used height so that value of indidual; height is added to the total_height variable when loop iterates
# # total_height = 0
# # for height in students_height:
# #   total_height += height
# # print(total_height)

# # # here used 1 because it will add the number of time the loop runs 
# # number_of_students = 0
# # for student in students_height:
# #   number_of_students +=1
# # print(number_of_students)

# # average = total_height / number_of_students

# # print(round(average))

# # This is spliting the string input  into a list datatype
# # students_scores = input("Input a list of students").split()
# # highest_score = 0
# # # This will convert the values from string to int
# # for n in range(0,len(students_scores)):
# #     students_scores[n] = int(students_scores[n])
# # print(students_scores)
# # # Don't use min and max 
# # for score in students_scores:
# #   if score > highest_score:
# #     highest_score = score
# # print(f"The highest score is {highest_score}")

# # Range
# # It will leave The last number ,the third parameter  is interval between numbers
# for number in range(1,10,3):
#   print(number) 


# # Add all numbers from 1 to 100
# # total = 0 
# # for number in range(1,100):
# #   total += number

# # print(total)


# # WAP to calculate the sum of even numbers from 1 to 100

# total = 0 
# for counter in range(1,101,2):
#    total += counter
# print(total)

# # Swecond way without range with interval
# totall = 0
# for counter in range(1,101):
#   if counter % 2 == 0:
#      totall += counter
# print(totall)




# # Interview Question
# # FizzBUZZ
# for counter  in range(1, 100):
#   if counter % 3 == 0 and counter % 5 == 0 :
#     print("FizzBUZZ") 
#   elif counter % 3 == 0 :
#     print("Fizz")
#   elif counter % 5 == 0 :
#      print("Buzz")
#   else:
#     print(counter)


# # Password Generator 
# letters = ['A', 'B' , 'C' , 'D' , 'E' , 'F' , 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
# symbols = ['!','#','$','%','&','(',')','*','+','-','^','`','~','|']
# numbers = ['0','1','2','3','4','5','6','7','8','9']
# print("Welcome to the Password Generator1")
# number_of_letters = int(input("How many letters would you like in your password?\n"))
# number_of_symbols = int(input("How many symbols would you like?\n"))
# total_number = int(input("How many numbers would you like?\n"))
# print(f"Here is your password")
# import random
# # Easy Level
# # password =""
# # # here 1 is added to add the exact nuumber in range 1-4 if 4 is slected 
# # for char in range(1,number_of_letters + 1):
# #   random_char = random.choice(letters)
# #   # print(random_char)
# #   password += random_char

# # for sym in range(1,number_of_symbols + 1):
# #   random_sym = random.choice(symbols)
# #   password += random_sym

# # for num in range(1,total_number + 1):
# #   random_num = random.choice(numbers)
# #   password += random_num

# # print(password)


# # Right Way  
# # We have to shuffle the order which can be done only in list so we changed passowrd to list 
# password = []
# # here 1 is added to add the exact nuumber in range 1-4 if 4 is slected 
# for char in range(1,number_of_letters + 1):
#   random_char = random.choice(letters)
#   # print(random_char)
#   password += random_char

# for sym in range(1,number_of_symbols + 1):
#   random_sym = random.choice(symbols)
#   password += random_sym

# for num in range(1,total_number + 1):
#   random_num = random.choice(numbers)
#   password += random_num

# print(password)

# random.shuffle(password)
# print(password)



# passwrd = ""

# for character in password:
#     passwrd += character
# print(f"Password Suggestion : {passwrd}")

# import dictionaries

import cypher
