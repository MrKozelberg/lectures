# -*- coding: utf-8 -*-
"""
Created on Fri May  7 00:37:56 2021

@author: Acer
"""

import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# constants
mu = 0.01
beta = 0
V = 1

fig = plt.figure()
ax_0 = fig.add_axes([0.2,0.15,0.7,0.7])

xi=np.linspace(-5,5,10000)
v = (4*V / (1+np.exp(3*xi/(4*mu))))**(1/3)

ax_0.set_xlim([-0.5,0.5])
ax_0.set_ylim([0,2])
ax_0.set_xlabel(r'$\xi$')
ax_0.set_ylabel(r'$v$')
ax_0.plot(xi,v,'r-', linewidth = 2, label = 'kink')

ax_0.legend()

ax_0.xaxis.set_major_locator(ticker.MultipleLocator(0.25))
ax_0.xaxis.set_minor_locator(ticker.MultipleLocator(2))
ax_0.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax_0.yaxis.set_minor_locator(ticker.MultipleLocator(2))

ax_0.grid(which='major',
        color = 'k')


ax_0.minorticks_on()
ax_0.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figwidth(5)
fig.set_figheight(3)

plt.show()

fig.savefig('kink.png', dpi = 200)