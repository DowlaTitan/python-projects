# to print statement in multiline 
# print(" hello \
# world")

# # arthemetic operators 
# x = 10
# y = 5
# print(x+y)
# print(x-y)
# print(x*y)
# print(x%y)
# print(x/y)
# print(x//y)
# print(x**y)


# # logical operators
# x = 10
# y = 5
# print(x and y)
# print(x or y)
# print(not y)


# # bitwise operators
# x = 10
# y = 5
# print(x&y)
# print(x|y)
# print(~x)
# print(x^y)
# print(x>>y)
# print(x<<y)

# # assignment operators 
# x = 5
# x+=2
# x-=2
# x*=2
# x%=2
# x//=2
# x**=2
# x&=2
# x|=2
# print(x)

# import os 
# print(os.getcwd())         # represents present working directory
# print(os.getcwdb())        # represents present working directory with bytes


# os.chdir()                        # to change the directory
# print(os.listdir())               # to list the all files and directories

# os.mkdir('test')                  # to create a directory 

# os.remove()                        # to remove a directory
# os.rmdir()                         # to remove a directory
# os.rename()                        # to rename a directory

# print(1,2,3,4,sep="*",end ="#")      # op ==>   1*2*3*4#


# print(" i love {0} and {1}".format('amma','nanna'))                # ==> I LOVE AMMA AND NANNA

# # math statement 
# x = int(input("x = "))
# print(x)
# import math                                    # sqauring of number 
# print(math.pow(int(x),2))

# a = int(input(" a = "))
# for i in range(1,a+1):
#     if a%i == 0:
#         print(i,end=" ")
#         i+=1


# # ascii values
# i = 32
# for i in range(256):
#     print(i,chr(i))

# # factorial number
# n = 5
# result = 1
# for i in range(1, n + 1):
#     result *= i
# print(result)    



num = [1,3,4,5,6,]
print(num[::-1])