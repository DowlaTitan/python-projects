# square root of number
import math
number = int(input(" enter number "))
value = math.sqrt(number)
print(value)


#  area and parimeter of a traingle 
side1 = int(input(" enter the side1 value "))
side2 = int(input(" enter the side2 value "))
side3 = int(input(" enter the side3 value "))
perimeter = side1+side2+side3
s = (side1+side2+side3)/2
area = s*(s-side1)*(s-side2)*(s-side3)
print(perimeter)
print(area)


# area and perimeter of a circle
radius = int(input(" enter the radius value "))
area = 3.14*radius*radius
print(area)
perimeter = 2*3.14*radius
print(perimeter) 


# quadratic equations
import cmath  # Importing cmath for complex number support

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Calculate the two roots
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Solve the equation
roots = solve_quadratic(a, b, c)

print(f"The roots are: {roots[0]} and {roots[1]}")
