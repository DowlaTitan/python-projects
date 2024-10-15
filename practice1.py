price = int(input(" enter the amount how much u spent "))
if price < 100:
    print(" u got 7 percent discount ")
elif 100 < price < 200:
    print(" u got 9 percent discount ")
elif 200 < price < 500:
    print(" u got 15 percent discount ")
elif price > 500:
    print(" u got 50 percent discount ")
else:
    print(" no discount for u ")