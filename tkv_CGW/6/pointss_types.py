#CGW 6
import numpy as np
from scipy.integrate import *
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# constants
mu = 1e-3
beta = 0.1
V = 1

fig_1 = plt.figure()
ax_1_0 = fig_1.add_axes([0.1,0.15,0.38,0.75])
ax_1_1 = fig_1.add_axes([0.6,0.15,0.38,0.75])

m = np.linspace(-5.0,5.0,10000)
b = - m**2 / (4*V)
b_ = np.linspace(-5,0,5000)
m_ = np.zeros(5000)

ax_1_0.set_title('$(0,\,0)$')
ax_1_0.set_xlim([-5,5])
ax_1_0.set_ylim([-5,5])
ax_1_0.set_xlabel(r'$\beta$')
ax_1_0.set_ylabel(r'$\mu$')
ax_1_0.plot(b,m, 'r-', linewidth = 3, label = '${\mu^2}/{4V}$')
ax_1_0.plot(b_, m_, 'y-', linewidth = 3, label = 'центр')
ax_1_0.text(-3,1,'устойчивый\n фокус',
            fontsize = 5)
ax_1_0.text(-3,-1.7,'неустойчивый\n фокус',
            fontsize = 5)
ax_1_0.text(-3,-4.7,'неустойчивый\n узел',
            fontsize = 5)
ax_1_0.text(-3, 4,'устойчивый\n узел',
            fontsize = 5)
ax_1_0.text(2, 0,'седло',
            fontsize = 10)
ax_1_0.fill_between(b, m, where=m>=0)
ax_1_0.fill_between(b, m, where=m<=0)
ax_1_0.fill_between(b, m, 5, where=m>=0)
ax_1_0.fill_between(b, m, -5, where=m<=0)

ax_1_0.legend()

ax_1_0.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax_1_0.yaxis.set_major_locator(ticker.MultipleLocator(1))

ax_1_0.grid(which='major',
        color = 'gray',
        linestyle = ':')

m = np.linspace(-10.0,10.0,100000)
b = m**2 / (12*V)
b_ = np.linspace(0, 5, 5000)

ax_1_1.set_title('$(0,\,\sqrt[3]{4V})$')
ax_1_1.set_xlim([-5,5])
ax_1_1.set_ylim([-5,5])
ax_1_1.set_xlabel(r'$\beta$')
ax_1_1.set_ylabel(r'$\mu$')
ax_1_1.plot(b,m, 'r-', linewidth = 3, label = '${\mu^2}/{12V}$')
ax_1_1.plot(b_, m_, 'y-', linewidth = 3, label = 'центр')
ax_1_1.text(3,-1.7,'уст.\n фокус',
            fontsize = 5)
ax_1_1.text(3, 1,'неуст.\n фокус',
            fontsize = 5)
ax_1_1.text(0.1, 4,'неуст.\n узел',
            fontsize = 5)
ax_1_1.text(0.1, -4.7,'уст.\n узел',
            fontsize = 5)
ax_1_1.text(-3, 0,'седло',
            fontsize = 10)
ax_1_1.fill_between(b, m, where=m>=0)
ax_1_1.fill_between(b, m, where=m<=0)
ax_1_1.fill_between(b, m, 5, where=m>=0)
ax_1_1.fill_between(b, m, -5, where=m<=0)

ax_1_1.legend()

ax_1_1.xaxis.set_major_locator(ticker.MultipleLocator(1))
ax_1_1.yaxis.set_major_locator(ticker.MultipleLocator(1))

ax_1_1.grid(which='major',
        color = 'gray',
        linestyle = ':')

fig_1.set_figwidth(8)
fig_1.set_figheight(3)

plt.show()

fig_1.savefig('00.png', dpi = 200)