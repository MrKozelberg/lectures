import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

ar = np.arange(1,10,0.2)

a = np.sqrt(ar*6470*2+ar**2)
b = np.sqrt(ar*6470*2)

fig = plt.figure()
ax_0 = fig.add_axes([0.2,0.15,0.7,0.7])

ax_0.set_xlim([1,9])
#ax_0.set_ylim([0,2])
ax_0.set_xlabel(r'$h$ [km]')
ax_0.set_ylabel(r'$l$ [km]')
ax_0.plot(ar,a,'r-', linewidth = 2, label = 'exact')
ax_0.plot(ar,b,'b--', linewidth = 2, label = 'approximate')

ax_0.legend()

ax_0.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax_0.xaxis.set_minor_locator(ticker.MultipleLocator(1))
ax_0.yaxis.set_major_locator(ticker.MultipleLocator(50))
ax_0.yaxis.set_minor_locator(ticker.MultipleLocator(1))

ax_0.grid(which='major',
        color = 'k')


ax_0.minorticks_on()
ax_0.grid(which='minor',
        color = 'gray',
        linestyle = ':')

fig.set_figwidth(9)
fig.set_figheight(6)

plt.show()