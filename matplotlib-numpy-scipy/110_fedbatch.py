#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Sat Jun 20 08:55:50 2020 @author: bjorn
## In[] <-remove one # 

# Solve Differential Equations in Python
# https://www.youtube.com/watch?v=VV3BnroVjZo
# https://github.com/j-m-mueller/Growth-Product-Estimator

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

µmax = 1       # 1/hour
Ks = 0.1       # g/liter
Yxs = 0.5      # g/g
Ypx = 10       # g/g
Sf = 10.0      # g/liter

alpha = 0.5
beta = 0.5

# https://www.rpi.edu/dept/chem-eng/Biotech-Environ/BatchProduction.htm

def F(t):
    return 1.0*t

def µ(S):
    return µmax*S/(Ks + S)

def rx(X,S):
    return µ(S)*X
    
def rp(X,S):
    return Ypx*rx(X,S)

def model(t,x):
    X,P,S,V = x
    dXdt = -F(t)*X/V + rx(X,S)
    dPdt = -F(t)*P/V + rp(X,S)
    dSdt = F(t)*(Sf-S)/V - rx(X,S)/Yxs
    dVdt = F(t)
    return [dXdt,dPdt,dSdt,dVdt]

X0,P0,S0,V0 = 4.0, 0.0, 5.0, 1.0

t0 = 0
tt = 10
t = np.linspace(t0,tt)

sol = solve_ivp( model,(t0,tt),[X0,P0,S0,V0],dense_output=True)

X,P,S,V = sol.sol(t)

# plot results

plt.plot(t,X)
plt.plot(t,P)
plt.plot(t,S)
plt.plot(t,V)

plt.xlabel('Time [hr]')
plt.ylabel('Concentration [g/liter]')
plt.legend(['X',
            'P',
            'S',
            'V'])
plt.show()