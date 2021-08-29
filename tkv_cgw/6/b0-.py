import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

mu = 0
beta = -1
V = 1
N = 10000
start = -5
final = 0

f = lambda x:np.sqrt(-beta)/np.sqrt(6*2**(1/3)/5*V**(5/3) - V*x**2 + x**5/10)
xi = np.zeros(N)
v = np.linspace(start,final,N)
for i in range(1,N):
    a = scipy.integrate.quad(f, start + (i-1)/N*(final-start),start + i/N*(final-start))[0]
    xi[i] = xi[i-1]+a

fig = plt.figure()
ax_0 = fig.add_axes([0.2,0.15,0.7,0.7])

#ax_0.set_xlim([0,5])
#ax_0.set_ylim([0,25])
ax_0.set_xlabel(r'$\xi$')
ax_0.set_ylabel(r'$v$')
ax_0.plot(v,xi,'r-', linewidth = 2, label = r'$v(\xi)$')

ax_0.legend()

# ax_0.xaxis.set_major_locator(ticker.MultipleLocator(5))
# ax_0.xaxis.set_minor_locator(ticker.MultipleLocator(2))
# ax_0.yaxis.set_major_locator(ticker.MultipleLocator(5))
# ax_0.yaxis.set_minor_locator(ticker.MultipleLocator(2))

# ax_0.grid(which='major',
#         color = 'k')


# ax_0.minorticks_on()
# ax_0.grid(which='minor',
#         color = 'gray',
#         linestyle = ':')

fig.set_figwidth(5)
fig.set_figheight(3)

plt.show()

fig.savefig('b0-.png', dpi = 200)
