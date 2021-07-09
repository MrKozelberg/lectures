import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

x, x_1, x_2, x_3, x_4, varkappa_1, varkappa_2, varkappa_3, varkappa_4 = sp.symbols('x, x_1, x_2,x_3, x_4, varkappa_1, varkappa_2, varkappa_3, varkappa_4')
var = x
start = -6
final = 6
k = [0.1,0.3,0.5,1]
N = 1000
n = 3
m = 4

Phi_1 = sp.cosh(varkappa_1*(x-x_1))
Phi_2 = sp.sinh(varkappa_2*(x-x_2))
Phi_3 = sp.cosh(varkappa_3*(x-x_3))
Phi_4 = sp.sinh(varkappa_4*(x-x_4))

wr_sol = sp.wronskian([Phi_1,Phi_2,Phi_3,Phi_4],var)
u_sp = 2*sp.diff(sp.log(wr_sol),var,2)
print(u_sp)

u_np = sp.lambdify((x, x_1, x_2, x_3, x_4, varkappa_1, varkappa_2, varkappa_3, varkappa_4),u_sp,modules="numpy")
x_ = np.linspace(start,final,N)

fig, axes = plt.subplots(n, m)

for i in range(0,n):
    for j in range(0,m):
        t = i*m+j
        u = u_np(x_,-1+t*k[0]**2,-2+t*k[1]**2,-3+t*k[2]**2,-4+t*k[3]**2,6,8,10,12)
        axes[i,j].set_xlim([start,final])
        axes[i,j].set_ylim([-0,300])
        axes[i,j].set_xlabel(r'$x$')
        axes[i,j].set_ylabel(r'$u$')
        axes[i,j].set_title("t={}".format(t))
        axes[i,j].plot(x_,u,'r-', linewidth = 2)
        axes[i,j].xaxis.set_major_locator(ticker.MultipleLocator(3))
        axes[i,j].xaxis.set_minor_locator(ticker.MultipleLocator(1))
        axes[i,j].yaxis.set_major_locator(ticker.MultipleLocator(100))
        axes[i,j].yaxis.set_minor_locator(ticker.MultipleLocator(1))
        axes[i,j].grid(which='major',
                     color = 'k')
        axes[i,j].minorticks_on()
        axes[i,j].grid(which='minor',
                     color = 'gray',
                     linestyle = ':')

fig.suptitle('Four Solitary Waves')
plt.subplots_adjust(wspace=0.4, bottom=0.05, hspace=0.3,top=0.93)

fig.set_figwidth(4*m)
fig.set_figheight(4*n)

fig.savefig('Figure_1.png', dpi = 200)     