import matplotlib.pyplot as plt
import numpy as np 


a = 3
b = 2
x0 = 1
y0 = 1


t = np.linspace(0,2*np.pi, 1000)
x = x0 + a*np.cos(t)
y = y0 + b*np.sin(t)

fig, ax = plt.subplots()
ax.plot(x,y)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('ellipse graph')

plt.show()