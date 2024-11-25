grade = int(input())
income = int(input())
sports = input()
backlogs = input( "(yes or no )")
if grade >= 80 and income <= 500000 and sports == "yes" and  backlogs == "no":
    print(" u r eligible for scholar ship ")
else:
    print(" u r not eligible  ")