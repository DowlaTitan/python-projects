valid = False

while not valid:
    user_input = input(" enter user name ")
    if len(user_input) >=5:
        valid = True 

print("user name is valid ", user_input)