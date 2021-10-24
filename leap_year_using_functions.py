# Leap Year 
# Condition
# year  % 4 == 0 
# year is not divisible by 100 unless it % 400 = 0
# year = int(input("Enter the year : "))


def isLeapYear(year):
  if year % 4 == 0 :
    if year % 100 == 0 :
      if year %  400 == 0:
         return True
      else: 
         return False
    else: 
       return True
  else: 
    return False

    