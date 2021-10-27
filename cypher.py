def greet():
  print("hi") 
  print("hello")  
  print("how are you")


# greet()

def greetOne(name):
  print(f"Hi {name}, how are you?")

greetOne("vibhor")

# functions with more than 1 parameters
def greet_with(name,location):
    print(f"Hi {name}, how are you?")
    print(f"What is like in {location}?")

# positional Argument
greet_with("Rahul", "New Delhi")

# to fix this
# Keyword Arguments
greet_with(location = "New Jersy",name = "Rahul")

import math
# PSET-2
test_h = int(input("Height of Wall: "))
test_w = int(input("width of Wall: "))
coverage = 5 


def calc(height,width,cover):
   result =  math.ceil((height * width) / cover )
   return print(f"You will need {result} cans of paint")

 
calc(height = test_h, width=test_w, cover=coverage)


# Prime number checker
# a number which is divided only by 1 and itself 

number = int(input("Enter a number: \n"))

def is_prime(number):
   is_prime_number = True
   for i in range(2,number):
       if number % i == 0:
          is_prime_number = False
   if is_prime_number:
      print("It's a prime number.")
   else:
      print("It's not a prime number.")


is_prime(number)