from scipy.optimize import newton
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from ode_functions.gating import *
from ode_functions.defaults import default_parameters
from ode_functions.current import nc



#Parameter values


hs=0.6
parameters=default_parameters(I_app=0.16)

vmin = -90
vmax = 50
vstep = 1
v = np.arange(vmin, vmax, vstep)

# dh nullcline:
dh_null = (h_inf(v))
plt.plot(v, dh_null)



null_solve = np.zeros((len(v), 2))

for i in range(len(v)):
    opt_fcn = lambda h: nc(h, v[i], parameters, hs=hs)
    h_solve = newton(opt_fcn, 0)  # calculate h value where dv=0

    # print(h_solve)

    null_solve[i, 0] = v[i]
    null_solve[i, 1] = h_solve

plt.plot(null_solve[:, 0], null_solve[:, 1], c="red")

hs = 0.2
null_solve = np.zeros((len(v), 2))

for i in range(len(v)):
    opt_fcn = lambda h: nc(h, v[i], parameters, hs=hs)
    h_solve = newton(opt_fcn, 0)  # calculate h value where dv=0

    # print(h_solve)

    null_solve[i, 0] = v[i]
    null_solve[i, 1] = h_solve

plt.plot(null_solve[:, 0], null_solve[:, 1], c="red")

hs = 0.05

null_solve = np.zeros((len(v), 2))

for i in range(len(v)):
    opt_fcn = lambda h: nc(h, v[i], parameters, hs=hs)
    h_solve = newton(opt_fcn, 0)  # calculate h value where dv=0

    # print(h_solve)

    null_solve[i, 0] = v[i]
    null_solve[i, 1] = h_solve

plt.plot(null_solve[:, 0], null_solve[:, 1], c="red")

plt.ylim(0, 0.4)
plt.xlim(-80, 40)
plt.xlabel("v_list (mV)")
plt.ylabel("h")
plt.legend(["h nullcline", "v_list nullcline (I_list=0.16, hs_list=0.6,0.2,0.05)"])