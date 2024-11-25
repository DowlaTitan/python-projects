# # # # # # # def is_power_of_two(n):
# # # # # # #     # A power of 2 is a positive number with exactly one bit set
# # # # # # #     if n <= 0:
# # # # # # #         return False
# # # # # # #     return (n & (n - 1)) == 0

# # # # # # # # Input from the user
# # # # # # # N = int(input("Enter an integer N: "))

# # # # # # # # Check if N is a power of 2 and output the result
# # # # # # # if is_power_of_two(N):
# # # # # # #     print(f"Yes, {N} is a power of 2.")
# # # # # # # else:
# # # # # # #     print(f"No, {N} is not a power of 2.")


# # # # # # # def power(n):
# # # # # # #     if n < 0:
# # # # # # #         return False
# # # # # # #     return (n & (n - 1)) == 0

# # # # # # # num = int(input(" enter a number "))
# # # # # # # if power(num):
# # # # # # #     print(" it is an power of two ")
# # # # # # # else:
# # # # # # #     print(" it is not the power of the two ")



# # # # # # for i in range(1500,2702):
# # # # # #     if i%7 == 0 and i%5 == 0:
# # # # # #         print(i)



# # # # # # armstrong
# # # # # n=int(input())
# # # # # k=len(str(n))
# # # # # num=n
# # # # # sum=0
# # # # # for i in range(k):
# # # # #     a=n%10
# # # # #     c=a**3
# # # # #     sum=sum+c
# # # # #     n=n//10
# # # # # if(sum==num):
# # # # #     print("ams")
# # # # # else:
# # # # #     print("not")



# # # # p=20
# # # # q=10
# # # # r=5
# # # # s=p*q/r+q%r-p
# # # # print(s)

# # # tempertures = []

# # # # for i in range(1,8):
# # # #     temp = float(input(" enter the temparuters "))
# # # #     tempertures.append(temp)

# # # #     avg=sum(tempertures)/len(tempertures)

# # # #     print(f" temparuters {temp}")

# # # temp = []

# # # for i in range(1,8):
# # #     temp = float(input(" enter a number "))
# # #     tempertures.append(temp)
# # #     avg = sum(tempertures)/len(tempertures)

# # #     print(f" {tempertures}")


# age = int(input(" enter a age "))
# movie = input(" enter a movie name ")
# ticket = input(" (yes or no)")
# if (age > 0 and movie == "G" and ticket == "yes"):
#     print(" u r going to G moovie ")
# elif (age > 0 and movie == "ka" and ticket == "yes"):
#     print(" u r going to ka movie ")
# else:
#     print(" u r not eligible for any movie ")



# n = int(input())
# sum = 0
# for i in range(n):
#     sum = sum + i
#     i += 1
#     print(sum)


# n = int(input(" enter "))
# result = 1
# i = 1
# for i in range(1,n):
#     result = result*i
#     i += 1
#     print(result)



# fruit = ["banana","apple","grapes","mango","guva"]
# print(fruit[3])

# print(len(fruit))

# print(fruit[5::-1])

# fruit1 = ["orange"]
# print(fruit+fruit1)


# del(fruit[3])
# print(fruit)

# fruit.remove("banana")
# print(fruit)

# print(len(fruit))