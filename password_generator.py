password = []
letters = ['A', 'B' , 'C' , 'D' , 'E' , 'F' , 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','#','$','%','&','(',')','*','+','-','^','`','~','|']
numbers = ['0','1','2','3','4','5','6','7','8','9']
print("Welcome to the Password Generator1")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
total_number = int(input("How many numbers would you like?\n"))
print(f"Here is your password")
import random
# here 1 is added to add the exact nuumber in range 1-4 if 4 is slected 
for char in range(1,number_of_letters + 1):
  random_char = random.choice(letters)
  # print(random_char)
  password += random_char

for sym in range(1,number_of_symbols + 1):
  random_sym = random.choice(symbols)
  password += random_sym

for num in range(1,total_number + 1):
  random_num = random.choice(numbers)
  password += random_num

print(password)

random.shuffle(password)
print(password)



passwrd = ""

for character in password:
    passwrd += character
print(f"Password Suggestion : {passwrd}")


