#CGW 6
import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# constants
mu = 1e-3
beta = 0.1
V = 1

# system
def f(u,t):
    x,y = u
    return [y, mu*y/beta + V/beta*x - x**4/(4*beta)]

# solution of ODE
t = np.linspace(0,5,10000)
u0=[2.149,0]
w = odeint(f,u0,t)
x = w[:,0]
y = w[:,1]

fig = plt.figure()
ax_0 = fig.add_axes([0.1,0.15,0.38,0.8])
ax_1 = fig.add_axes([0.6,0.15,0.38,0.8])

ax_0.set_xlim([0,5])
ax_0.set_ylim([-0,3])
ax_0.set_xlabel(r'$\xi$')
ax_0.set_ylabel(r'$v$')
ax_0.plot(t,x,'r-', linewidth = 2, label = 'our solution')
ax_0.plot(t,(10*V)**(1/3)/(np.cosh(3/2*np.sqrt(V/beta)*t))**(2/3),
           'b--', linewidth = 1, label = 'soliton')

ax_0.legend()

ax_0.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax_0.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax_0.yaxis.set_major_locator(ticker.MultipleLocator(0.5))
ax_0.yaxis.set_minor_locator(ticker.MultipleLocator(1))

ax_0.grid(which='major',
        color = 'k')


ax_0.minorticks_on()
ax_0.grid(which='minor',
        color = 'gray',
        linestyle = ':')

ax_1.set_xlim([0,2.3])
ax_1.set_ylim([-4.5,4.5])
ax_1.set_xlabel(r'$v$')
ax_1.set_ylabel(r"$v'$", )

ax_1.plot(x,y,'r-',linewidth = 2, label = 'our solution')

for i in range(1,10):
  t = np.linspace(0,3,10000)
  u0=[0.05+i/4,0]
  w = odeint(f,u0,t)
  x = w[:,0]
  y = w[:,1]
  
  ax_1.plot(x,y,'b-',linewidth = 1)

for i in range(1,5):
  t = np.linspace(0,2,10000)
  u0=[0,0.05+i]
  w = odeint(f,u0,t)
  x = w[:,0]
  y = w[:,1]
  
  ax_1.plot(x,y,'b-',linewidth = 1)

ax_1.legend()

fig.set_figwidth(8)
fig.set_figheight(3)

plt.show()

fig.savefig('plot_and_phase_plane.png', dpi = 600)