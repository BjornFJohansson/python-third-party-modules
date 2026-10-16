#!/usr/bin/env python
# coding: utf-8
"""docstring."""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Solve an initial value problem (solve_ivp) for a system of ODEs.
# This function numerically integrates a system of ordinary
# differential equations given an initial value:
# dy / dt = f(t, y)
# y(t0) = y0


y0 = 0.0
c = 1.0

def model(t, vals):
    """docstring."""
    # dy
    # -- = c
    # dt
    dydt = c
    return [dydt]


# time points
t0 = 0
tt = 4
t = np.linspace(t0, tt)

# solve ODE
result = solve_ivp(model, (t0, tt), [y0], dense_output=True)

y = result.sol(t)[0]

# plot results
plt.plot(t, y)

plt
