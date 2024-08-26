a = [['roy',80,78,67,90,78],
     ['john',78,98,26,78,45],
     ['jack',23,34,45,56,67]]

b = [['roy',80,78,67,90,78],
     ['john',78,98,26],
     ['jack',23,34,45,56,67]]
print(a)
print()
print(b)


n = 3
m = 4
a = [m] * n
print(a)
for i in range(n):
    a[i] = [0] * m
print(a)
print(a[1])

a[1][3] = 75
print(a)