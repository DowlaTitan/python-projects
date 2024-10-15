dict = { x : x*x for x in range(9)}
print(dict)

print(1 in dict)
print(8 not in dict)


square = {1:1,2:4,3:9,4:16,5:25}
for i in square :
    print(square[i])


square = {1:1,2:4,3:9,4:16,5:25}
# prints the lenth of dictonary 
print(len(square))
# printts elements in the order 
print(sorted(square))