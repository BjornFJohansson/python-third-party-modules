#!/usr/bin/env python
# coding: utf-8
"""docstring."""

from math import log
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# initial condition
X0 = 0.2

# Set generation time
td = 0.5
µmax = log(2)/td
print(µmax)  # Growth rate (h-1)

def model(t, values):
    """Return dX/dt."""
    X = values[0]
    dXdt = µmax * X
    return [dXdt]

# time points
t0 = 0
tt = 4
t = np.linspace(t0, tt)

# solve ODE
result = solve_ivp(model, (t0, tt), [X0, ], dense_output=True)

X = result.sol(t)[0]

# plot results
plt.plot(t, X, "r-", linewidth=2, label=f"mu={µmax}")
plt.xlabel("time")
plt.ylabel("X(t)")
plt.legend()
plt.show()
