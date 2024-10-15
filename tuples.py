tuple1 = ('w','e','l')
tuple2 = ('c','o','m','e')
tuple3 = tuple1 + tuple2
print(tuple3)
print(tuple3 * 3)

print(tuple3.count('m'))
print(tuple3.index('m')) 

print('z' in tuple3)
print('w' in tuple3)

for letters in tuple3:
    print(letters)