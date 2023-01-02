
# # import greet
# # import paint

# # from prime import is_prime

# # Cypher


# alphabet = ['A', 'B' , 'C' , 'D' , 'E' , 'F' , 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# direction = input("Type 'encode' to encrypt ,type 'decrypt' to decrypt: \n")
# text = input("Type your message :  \n")
# shift = int(input("Type your shift number :  \n"))

# def encrypt(text,shift):
  
#   message = ""
#   for letter in text:
#     position = alphabet.index(letter)
#     new_position = position + shift 
#     new_text = alphabet[new_position]
#     message += new_text

#     print(f"The encrypted text is {message}")

# encrypt(text=text,shift=shift)

# def decrypt(text,shift):
#     pass


# decrypt(text=text,shift=shift)

