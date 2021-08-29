import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# constants
mu = 0
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
ax_1 = fig.add_axes([0.15,0.15,0.8,0.75])

ax_1.set_title('beta>0')
ax_1.set_xlim([0,2.3])
ax_1.set_ylim([-4.5,4.5])
ax_1.set_xlabel(r'$v$')
ax_1.set_ylabel(r"$v'$", )

ax_1.plot(x,y,'b-',linewidth = 1)

for i in range(1,10):
  t = np.linspace(0,3,10000)
  u0=[0.3+i/5,0]
  w = odeint(f,u0,t)
  x = w[:,0]
  y = w[:,1]
  
  ax_1.plot(x,y,'b-',linewidth = 1)


for i in range(1,10):
  t = np.linspace(0,3,10000)
  u0=[0,i/10*5]
  w = odeint(f,u0,t)
  x = w[:,0]
  y = w[:,1]
  
  ax_1.plot(x,y,'b-',linewidth = 1)

fig.set_figwidth(4)
fig.set_figheight(3)

plt.show()

fig.savefig('0-.png', dpi = 200)