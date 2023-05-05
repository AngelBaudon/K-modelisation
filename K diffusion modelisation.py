# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 17:46:32 2023

@author: Angel.BAUDON
"""
import numpy as np, matplotlib.pyplot as plt


U = 10e-8 # Volume ejected (L)
Cf = 3*10e-2 # Initial concentration of the substance (Molar)
Lx, Ly, Lz = .1, 1.54, 1.54
L = Lx * Ly * Lz # lambda, tortuosity
a = .21 # alpha, volume fraction of the tissue (no unit, %)
D = 11.1 * 10e-6 # free diffusion coeficient
pi = np.pi
r = 10e-2 # distance (cm)
k = .1 # first order kinetic constant

def C(t):
    C = ((U*Cf*L)/(a*(4*D*t*pi)**(2/3))) * np.exp(-((L**2 * r**2)/(4*D*t))-k*t)
    return C * 1000 * 1000

K = np.zeros((20, 40))
for i in range(20): K[i,i:] = [C(t) for t in range(1, 41-i)]

plt.figure(), plt.plot(np.sum(K, axis = 0))
plt.ylabel('Concentration (mM)'), plt.xlabel('Time (s)')
print(max(np.sum(K, axis = 0)))



