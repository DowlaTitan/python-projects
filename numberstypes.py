value1 = 100
print(type(value1))
print(float(value1))
print(isinstance(value1,int))
print(isinstance(value1,float))
print(isinstance(value1,complex))
print(complex(value1))

print(0b1101)
print(0xab)
print(0o23)


print(10 + 13.4)

data1 = 0.1 + 0.2
print(data1)
data1 = 1.2 + 2.4 
print(data1)
from decimal import Decimal as D
print(D('0.1') + D('0.2'))
print(D('1.2') + D('2.4'))

from fractions import Fraction as F
print(F(1.3))
print(F(2.3))
print(F(9.6))

import math 
print (math.pi)
print (math.sin(10))
print (math.cos(10))
print (math.log10(10))
print (math.factorial(5))
print (math.exp(10))



import random
days = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
print(random.choice(days))