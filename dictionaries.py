dictionary = {
  "A":"First Letter",
  "B":"Second Letter",
  "C":"Third Letter",

}

print(dictionary['A'])
print(dictionary['B'])
print(dictionary['C'])

dictionary["D"] = "Fourth Letter"

print(dictionary)

# This will return key
for a in dictionary:
  print(a)


# This will return value
for a in dictionary:
  print(dictionary[a])
  
# PSet-1
student_scores = {
  "Vibhor" : 81,
  "Rahul" : 34,"Richa" : 88,"Aman" : 77,"Akhil" : 99,
}

student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 91 and score < 100 :
      student_grades[student]="Outstanding"
  elif score > 81 and score < 90 :  
      student_grades[student]="Exceeds Expectations"
  elif score > 71 and score < 80 :  
       student_grades[student]="Acceptable"
  elif score <= 70 :  
       student_grades[student]="Fail"
print(student_grades)

# Nesting
capitals = {
  "France" : "Paris",
  "India" : "New Delhi"
}

#  Nesting list in a Dictionary

travel_log  = {
  "India" : ["New Delhi","Bangalore","Chandigarh"],
  "America" : ["Kentucky", "Las Vegas", "Los Angeles"]

}

# #  Nesting Dictionary in a Dictionary
# travel_log  = {
#   "India" : { 
#     "city_visited" : ["Bangalore","New Delhi"]
#   ,"total_visits": 12},
#   "America" : {   "city_visited" :["Kentucky" , "Las Vegas", "Los Angeles"],"total_visits": 12}
# }

# # Dictioonary in a list 
# travel_log  = [
#   {"country" : "India" ,
#     "city_visited" : ["Bangalore","New Delhi"]
#   ,"total_visits": 12},
#   {"country" : "America" ,
#      "city_visited" :["Kentucky" , "Las Vegas", "Los Angeles"],"total_visits": 12}
# ]



travel_log = [
  {
    "country": "France",
    "visits":12,
    "cities":["Paris","Lille","Dijhon"]

  },
  {
    "country":"Germany",
    "visits":6,
    "cities":["Berlin","Hamburg","Stuttgart"]
  }
]
# Dont Change The above data
# add new counry as a dictionary and then add new country to the list as list using a function append 
def add_new_country(country,visits,cities):
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = visits
  new_country["cities"] = cities
  travel_log.append(new_country)





add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)


from replit import clear
# from art import logo

# print(logo)
# PS-3
bids={}
isBidding = False

# CHecking For Higher Bid
def checkHighestBid(record):
  highest_bid = 0 
  winner = ""
  # {"Vibhor." : 12345 , "Helna" :"3333"}
  for bid_value in record:
     bid_amount = record[bid_value]
     if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bid_value
  print(f"The winner of the bid is {winner} with bid of ₹{highest_bid}")



while not isBidding:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bids[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if should_continue == "no":
      isBidding = True
      checkHighestBid(bids)
    elif should_continue == "yes":
      clear()




