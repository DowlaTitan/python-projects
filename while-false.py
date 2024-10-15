valid = False

while not valid:
    user_input = input("Enter your username: ")
    if len(user_input) >= 5:
        valid = True 

print("Username accepted:", user_input)
 