while True:
    user_input = input("Enter a number greater than 10: ")
    number = int(user_input)
    if number > 10:
        break  

print("Valid number entered:", number)