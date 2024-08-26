set1 = {12,23,34,45,56}
set2 = {1,12,23,34,45}

print(set1)
print(set2)

# for addition
print(set1 | set2)
print(set2 | set1)
print(set2.union(set1))
print(set1.union(set2))

# for intersection
print(set1 & set2)
print(set1.intersection(set2))


# for differance
print(set1 - set2)
print(set2 - set1)
print(set1.difference(set2))


# for symmetric differance 
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# set membership
print(12 in set1)
print(243 in set1) 

# ierating through set
for letter in set("welcome"):
    print(letter)