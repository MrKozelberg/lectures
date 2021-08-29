# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 08:47:13 2021

@author: Acer
"""

from sympy import *

omega_0, Omega, D, d, alpha, n_1, n_2, n, m, A, A_1 = symbols('omega_0, Omega, D, d, alpha, n_1, n_2, n, m, A, A_1', real = True)
A_0 = symbols('A_0', real = True)

D = (omega_0**2-Omega**2*(1+3*sqrt(2)))/(10*sqrt(2)*omega_0)
d = sqrt(5)/4*sqrt((4+2*sqrt(2))*Omega**2-omega_0**2)
A_1 = A_0/(omega_0*sqrt(4*Omega**2-omega_0**2))
A2 = 2*sqrt(10)*A_0**2*exp(-alpha*omega_0**2*(2*m - n)**2*(2*Omega**2*(sqrt(2) + 2) - omega_0**2)/(alpha**2*n**2*(Omega**2*(1 + 3*sqrt(2)) - omega_0**2)**2 + 2*omega_0**2*(2*Omega**2*(sqrt(2) + 2) - omega_0**2)))/(5*omega_0*sqrt(alpha**2*n**2*(Omega**2*(1 + 3*sqrt(2)) - omega_0**2)**2 + 2*omega_0**2*(2*Omega**2*(sqrt(2) + 2) - omega_0**2))*(4*Omega**2 - omega_0**2))

A2 = (((A2.subs(omega_0,sqrt(2))).subs(Omega,1)).subs(alpha,1)).subs(A_0,1)

from sympy.plotting import plot, plot3d
print('|A|^2 from (n,m)')
p1 = plot3d(A2, (n,0,20), (m,-50,50), nb_of_points_x=100, nb_of_points_y = 100)
#p2 = plot3d(A2, (n,0,20), (m,0,100), nb_of_points_x=100, nb_of_points_y = 100)

A2 = 2*sqrt(10)*A_0**2*exp(-alpha*omega_0**2*(2*m - n)**2*(2*Omega**2*(sqrt(2) + 2) - omega_0**2)/(alpha**2*n**2*(Omega**2*(1 + 3*sqrt(2)) - omega_0**2)**2 + 2*omega_0**2*(2*Omega**2*(sqrt(2) + 2) - omega_0**2)))/(5*omega_0*sqrt(alpha**2*n**2*(Omega**2*(1 + 3*sqrt(2)) - omega_0**2)**2 + 2*omega_0**2*(2*Omega**2*(sqrt(2) + 2) - omega_0**2))*(4*Omega**2 - omega_0**2))
A2 = ((((A2.subs(n,0)).subs(Omega,1)).subs(alpha,1)).subs(A_0,1)).subs(m,0)
#print('|A|^2 from omega_0')
#p3 = plot(A2, (omega_0, 2-sqrt(2)+0.1, 2-sqrt(2)-0.1))
