age = int(input(" enter which number u want "))

if age  < 5:
    print(" age is above 5 years ")
elif age == 5:
    print(" age is is equal to 5 years ")
elif((age > 5) and (age < 17)):
    grade = age - 5 
    print(" u can go to grade {}  ".format(grade))
else :
    print(" u can go to college ")