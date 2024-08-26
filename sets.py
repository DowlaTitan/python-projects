set1 = {22,34,45}
print(set1)

set2 = {22,34,'hello',90}
print(set2)

set1.add(77)
print(set1)
set1.update([12,45,67])
print(set1)

set1.discard(77)
print(set1)
set1.remove(22)
print(set1)

print(set1.pop())
print(set1.pop())

set1.clear
print(set1)