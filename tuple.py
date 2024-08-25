# creating empty tuple
tuple1 = ()
print(tuple1)

# creating integers with tuple
tuple2 = (1,2,3)
print(tuple2)

# creating all data types with tuple
tuple3 = (1,'all tuple',34,'all')
print(tuple3)

tuple4 = ("nested",[12,34,45],(12,78))
print(tuple4)


# tuple canb be creating with out paranthesis 
# it can be called packing tuple 
tuple5 = 101,"hello",78.09,"jai"
print(tuple5)

# tuple unpacking is available 
jack,guruji,cable,foot = tuple5
print(jack)
print(guruji)
print(cable)
print(foot)

print(type(tuple5))
