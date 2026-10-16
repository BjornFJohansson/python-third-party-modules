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

µmax  = 0.5     # 1/hour
Ks    = 0.01     # g/liter
Yxs   = 0.5     # g/g
Ypx   = 0.5       # g/g
Sin   = 5.0     # g/liter
D     = 0.1     # h-1
V     = 1.0

def µ(S):
    return µmax*S/(Ks + S)

def rx(X,S):
    return µ(S)*X
    
def rp(X,S):
    return Ypx*rx(X,S)

def rs(X,S):
    return -1/Yxs*rx(X,S)

def model(t,x):
    X,P,S = x
    dXdt =  rx(X,S)*V - D*X
    dPdt =  rp(X,S)*V - D*P 
    dSdt =  rs(X,S)*V + D*(Sin-S)
    return [dXdt,dPdt,dSdt]

X0,P0,S0 = 1.0, 0.0, 1.0

t0 = 0
tt = 15
t = np.linspace(t0,tt)

sol = solve_ivp( model,(t0,tt),[X0,P0,S0],dense_output=True)

X,P,S = sol.sol(t)

# plot results

plt.plot(t,X)
plt.plot(t,P)
plt.plot(t,S)
plt.plot(t,µ(S))

plt.xlabel('Time [hr]')
plt.ylabel('Concentration [g/liter]')
plt.legend(['X',
            'P',
            'S',
            'µ'])
plt.show()