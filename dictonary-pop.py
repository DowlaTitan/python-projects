square = { 1:1,2:4,3:9,4:16,5:25}
print(square)

# remove particular item
print(square.pop(4))
print(square)

# romove an arbitary item
print(square.popitem())
print(square)

# deelting items
del square[1]
print(square)