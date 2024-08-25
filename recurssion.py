def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

print(" factorial value is ",fact(6))