#CGW 8
import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

t_start=0
t_final=4
N = 1000
t = np.linspace(t_start,t_final, N)
ax_min = 0
ax_max = 5
bx_max = 3
bx_min = -3

def sys(t, u, alpha, P_0, k_0):
    a_x, b_x, a_y, b_y = u
    return [b_x, 4/a_x**3 * (1 - a_x /(4*np.pi*a_y) * 
                            P_0),
            b_y, 4/a_y**3 * (1 - a_y /(4*np.pi*a_x) * 
                            P_0)]

fig = plt.figure()
ax_0 = fig.add_axes([0.1,0.15,0.38,0.8])
ax_1 = fig.add_axes([0.6,0.15,0.38,0.8])

ax_0.set_xlim([ax_min,ax_max])
ax_0.set_ylim([bx_min,bx_max])
ax_0.set_xlabel(r'$a_x$')
ax_0.set_ylabel(r"$b_x$", )

ax_1.set_xlim([ax_min,ax_max])
ax_1.set_ylim([bx_min,bx_max])
ax_1.set_xlabel(r'$a_y$')
ax_1.set_ylabel(r"$b_y$")

n = 2

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            for l in range(1,n+1):
                u_0 = [ax_min+i/n*(ax_max-ax_min),bx_min+j/n*(bx_max-bx_min),
                       ax_min+k/n*(ax_max-ax_min),bx_min+l/n*(bx_max-bx_min)]
                sol = solve_ivp(sys, [t_start, t_final], u_0,
                                args=(1, 25, 0.1),
                                dense_output=True)
                z = sol.sol(t)
                ax_0.plot(z[0].T,z[1].T,'-',linewidth = 1, label = r'phase plane $a_x$')
                ax_1.plot(z[2].T,z[3].T,'-',linewidth = 1, label = r'phase plane $a_y$')
plt.show()                
