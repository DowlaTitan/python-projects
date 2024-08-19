try:
    a = int(input(" enter a value "))
    b = int(input(" enter b value "))
    c = a/b
    print("  {} / {} = {} ".format(a,b,c))
except ZeroDivisionError:
    print(" zero division error is terminated ")