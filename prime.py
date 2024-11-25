# def prime(n):
#     if n <= 1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i == 0:
#             return False
#         return True


# num = int(input(" enter a number "))
# if prime(num):
#     print(" it is a prime number  ")
# else:
#     print(" it is not a prime number ")


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end='')
#     print()







# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end='')
#     print() 

# k=0
# for i in range(1,6):
#     for j in range(1,i+1):
#         k=k+1
#         print(k,end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(6-i,0,-1):
#         print(j,end=' ')
#     print()

# for i in range(1,6):
#     print(' '*(6-i),end='')
#     for j in range(1,i+1):
#         print(j,end='')
#     print()


for i in range(1,6):
    print(' '*(6-i),end='')
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
# for i in range(1,6):
#     print(' '*(6-i),end='')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
# print()

# v=1
# for i in range(1,6):
#     print(" "*(6-i),end=" ")
#     for j in range(i+1):
#         print(v,end=" ")
#         v=v*((i-j)//(1+j))
#         print()
# print()       
 
# n=int(input('enter a value'))        
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
# for i in range(n-1,0,-1):
#     print(' '*(n-i),end='')
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()