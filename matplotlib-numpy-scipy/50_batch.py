#!/usr/bin/env python
# coding: utf-8

# https://www.youtube.com/watch?v=VV3BnroVjZo
# http://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# https://www.youtube.com/watch?v=8-V5T40aMEc
# https://github.com/j-m-mueller/Growth-Product-Estimator

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

µmax = 0.31  # h-1
Ks = 10       # 0.1  # g/L
Yxs = 0.5    # g biomass / g substrate


def µ(S):
    """Return µ."""
    return µmax * S / (Ks + S)


def model(t, vals):
    """Return dX/dt dS/dt and dP/dt."""
    X, S = vals
    dXdt = µ(S) * X
    dSdt = -dXdt * 1 / Yxs
    return [dXdt, dSdt]


# initial condition

X0 = 0.1 # g/L
S0 = 18  # 18 g/L

# time points

t0 = 0
tt = 48

t = np.linspace(t0, tt)

sol = solve_ivp(model, (t0, tt), [X0, S0], dense_output=True)

X, S = sol.sol(t)

# plot results

plt.figure(figsize=(5, 5))
ax = plt.gca()
# ax.set_aspect(0.5)
plt.plot(t, X, "g")
plt.plot(t, S, "b")

plt.xlabel("Time [hr]")
plt.ylabel("Concentration [g/liter]")
plt.legend(["X", "S"])
plt.show()
