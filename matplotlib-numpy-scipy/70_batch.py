#!/usr/bin/env python
# coding: utf-8

# https://www.youtube.com/watch?v=VV3BnroVjZo
# http://apmonitor.com/pdc/index.php/Main/SolveDifferentialEquations
# https://www.youtube.com/watch?v=8-V5T40aMEc
# https://github.com/j-m-mueller/Growth-Product-Estimator

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


S0 = 90      # 18 g/L
µmax = 0.08  # h-1
X0 = 2.0
Yxs = 0.6    # g biomass / g substrate
α = 0.9
β = 0.1
P0 = 0
Ks = 0.5       # 0.1  # g/L


def µ(S):
    """Return µ."""
    return µmax * S / (Ks + S)


def model(t, vals):
    """Return dX/dt dS/dt and dP/dt."""
    X, S, P = vals
    dXdt = µ(S) * X
    dPdt = α * dXdt + β * X
    dSdt = - (1/Yxs) * dXdt
    return [dXdt, dSdt, dPdt]


# time points

t0 = 0
tt = 36

t = np.linspace(t0, tt)

sol = solve_ivp(model, (t0, tt), [X0, S0, P0], dense_output=True)

X, S, P = sol.sol(t)

# plot results

plt.figure(figsize=(5, 5))
ax = plt.gca()
plt.plot(t, X, "green")
plt.plot(t, S, "blue")
plt.plot(t, P, "red")

plt.xlabel("Time [hr]")
plt.ylabel("Concentration [g/liter]")
plt.legend(["X", "S", "P"])
plt.show()











