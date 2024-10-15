list = [11,22,33,44]
our_list = iter(list)

print(next(our_list))

print(next(our_list))

print(our_list.__next__())
print(our_list.__next__())