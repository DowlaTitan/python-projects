def add(x,y):
    return x + y 
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
def div(x,y):
    if y == 0:
        return "divison is error "
    return x / y


def caluculater():
    print(" choose which otion u want ")
    print(" 1: additon ")
    print(" 2: substraction ")
    print(" 3: multiplication ")
    print(" 4: division ")


choice = input(" choice u r optioon ")
if choice in ['1','2','3','4','5']:
    num1 = int(input(" enter number1 "))
    num2 = int(input("enter number 2 vaule"))

    operations = {
        '1' : add,
        '2' : sub,
        '3' : mul,
        '4' : div
    }

    result = operations[choice](num1,num2)
    print(f"the result is: {result}")
else:
    print("invalid input ")