import hashlib

#Getting user input
user_input = input("Enter a message: ")

#Encoding user input
encoded_user_input = user_input.encode()

#Hashing user input
hash = hashlib.sha256(encoded_user_input)

print(hash.hexdigest())