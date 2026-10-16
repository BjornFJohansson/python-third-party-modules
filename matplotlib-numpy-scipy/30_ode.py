#!/usr/bin/env python
# coding: utf-8
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Solve an initial value problem (solve_ivp) for a system of ODEs.
# This function numerically integrates a system of ordinary 
# differential equations given an initial value:
    
# dy / dt = f(t, y)
# y(t0) = y0

y0 = 1
x0 = 1
c = 1.5

def model(t, vals):
    # dy
    # -- = c
    # dt
    dydt = c
    dxdt = -c
    return [dydt, dxdt]

# time points
t0 = 0
tt = 4
t = np.linspace(t0, tt)

# solve ODE
result = solve_ivp(model, (t0, tt), [y0,x0], dense_output=True)

y,x = result.sol(t)

# plot results
plt.plot(t, y)
plt.plot(t, x)
