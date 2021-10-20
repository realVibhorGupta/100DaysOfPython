# DAY -1
print("Hello World")


# WAP To show the output as provided!

print('what to print')

# Use of nextline Characters

print("Hi !!\n How \tare \byou !!How\f is\r everything\t going\v? ")

# String Concatenation
print("hello" + "Vibhor")

# Finishing String Concatenation
print("hello" + " " + "Vibhor")

# P-2
print("DAY 1 -  STRING MAIPULATION")
print("String Concatenation is fone with the "+" " + "sign.")
print ("e.g print(" + "Hello" + " "  +"world)")
print("New lines can be created with a \n Hurray") 


# input the  data
# input("What is your name?\n")

# P-3

# name = input("What is your name?\n")
# print(len(name))

# Variables
name= "Vibhor"
print(name)

# P=4
# SWAP the values of the variables a and b using user input

# take two varaibles a znd B 
# we take another variable c 
# store the values of let us say b into c and then intert=change the valuyes 
# finally store The value of c to the the remaining variable

# a = input("Inpout The value of a=")
# b = input("Inpout The value of b=")
# c = a
# a = b 
# b = c 
# print("the value of a : "+ a + "\n" + "the value of b : "+ b)

# Data Types
# Int ,  String  ,Float , Boolean 
# print("Hello"[4])
# print("123"+"456")

# # Fix Type Error
# num_char = len(input("What is your name?\n"))
# # print("Your name has " + num_char + "characters.")
# print(type(num_char))
# # Type Casting

# print("Your name has " + str(num_char) + " characters.")
print(70 + float(100.5))
print(str(70) + str(100.5))

# P5
# WAP that adds digits in a 2 digit number . If the input was 24 , the output should be 6

# a  = input("Enter the first number a: ")
# first_digit = a[0]
# second_digit = a[1]
# result = int(first_digit)+ int(second_digit)
# print("the value of "+ str(result))


# PEMDAS equalivlent to BODMAS in Maths
# PS-6
# Calculate The BMI
# height = input("Enter your height in m: ")
# weight = input("Enter your weight in kg: ")

# bmi = int(weight) / float(height) ** 2
# print("bmi is: " + str(bmi) )

# Number Manipulation and F Strings 
print(int(8/3))

print(round(8/3,8))

print(type(8 // 3))

# String Inetrpolation use {} in the String with using f""eg . f" foo {value}"


# Control Statements

# print("Welcome to Code")
# height = int(input("What is your height in cm : "))
# if height > 120 :
#     print("you can ride")
# else:
#   print("you cannot ride")

# #  Code Challenge 
# # ODD or EVEN

# odd_or_even = int(input("Enter any number : "))
# if odd_or_even % 2 == 0 :
#   print(f"Number {odd_or_even} is even")
# else:
#   print(f"Number {odd_or_even} is odd")

# BMI Excercise 2 
# height = float (input("enter your height in meters : "))
# weight = float (input("enter your weight in kilograms : "))
# bmi = round(weight/height ** 2)
# if bmi < 18.5 :
#   print(f"Your bmi is {bmi} and you are underweight.")
# elif bmi < 25:
#   print(f"Your bmi is {bmi} and you are normal weight.")
# elif bmi < 30  :
#    print(f"Your bmi is {bmi} and you are over weight.")
# elif bmi < 35 :
#    print(f"Your bmi is {bmi} and you are obese.")
# else :
#    print(f"Your bmi is {bmi} and you are clinically obese.")


# Leap Year 
# Condition
# year  % 4 == 0 
# year is not divisible by 100 unless it % 400 = 0
# year = int(input("Enter the year : "))
# if year % 4 == 0 :
#   if year % 100 == 0 :
#     if year %  400 == 0:
#         print("It is  a leap year")
#     else: 
#       print("It is not a leap year")
#   else: 
#     print("It is not a leap year")
# else: 
#   print("It is not a leap year")

# Pizza Order Excercise

# print("Welcome to Python Pizza Delivery")
# size = input("What size pizza do you want? S ,M , L")
# add_peparoni = input("Do you want peparoni? Y or N")
# add_extra_cheese = input("Do you want extra_cheese? Y or N")

#Randomization
import random

random_integer = random.randint(1,10)
print(f"random number between 1 and 10 is {random_integer}")

random_float = random.uniform(1,5)
print(f"random float number between 1 and 5 is {random_float}")


#Head or Tail  Game 
head_or_tail = random.randint(0,1)
if  head_or_tail == 1:
  print("Tails")
else:
  print("Head")




# choice   = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

