""" A first plot - get some numbers."""

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [1,23,2,4])
plt.ylabel('some numbers')
plt.show()

""" NumPy ."""

import numpy as np

t0 = 0
tt = 100

t = np.linspace(t0,tt)

t

# Data for plotting

t = np.arange(0.0, 2.0, 0.01)

s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()

ax.plot(t, s)

ax.set(xlabel='time (s)',
       ylabel='voltage (mV)',
       title='Simple')
ax.grid()

plt
