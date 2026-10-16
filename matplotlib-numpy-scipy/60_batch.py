#!/usr/bin/env python
# coding: utf-8

# https://www.youtube.com/watch?v=VV3BnroVjZo
# http://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# https://www.youtube.com/watch?v=8-V5T40aMEc
# https://github.com/j-m-mueller/Growth-Product-Estimator

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

µmax = 0.693147180559945  # h-1
Yxs = 0.5  # g biomass / g substrate
Ypx = 0.5  # g product / g biomass produced


def model(t, vals):
    """Return dX/dt, dS/dt and dP/dt."""
    X, S, P = vals
    dXdt = µmax * X
    dPdt = Ypx * dXdt
    dSdt = - (1 / Yxs) * dXdt - (1 / Ypx) * dPdt
    return [dXdt, dSdt, dPdt]

# initial condition
X0 = 4
S0 = 20
P0 = 0

# time points

t0 = 0
tt = 2.1

t = np.linspace(t0, tt)

result = solve_ivp(model, (t0, tt), [X0, S0, P0], dense_output=True)

X, S, P = result.sol(t)

# plot results

plt.figure(figsize=(5, 5))
ax = plt.gca()
plt.plot(t, X, "g")
plt.plot(t, S, "b")
plt.plot(t, P, "r")

plt.xlabel("Time [hr]")
plt.ylabel("Concentration [g/liter]")
plt.legend(["X", "S", "P"])
plt.show()
