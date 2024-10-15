import random as r
rand_num = r.randrange(1,19)
print(" the number is ",rand_num)
i = 1
while True:
    print(" number guessed ",i)
    if(i == rand_num):
        print(" random number is printed succesfully ")
        break
    i += 1