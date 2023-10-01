import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

x = np.linspace(0, 10, 1000)
O = 0.5
d = 0.4
o = np.sqrt(4*O**2+d**2)

def fun(x):
    return 4*O**2/o *np.sin(o*x/2)**2

def re(x):
    return 2 * O * d/o * np.sin(o/2*x)**2

def im(x):
    return O*np.sin(o*x)

mpl.rc('xtick', labelsize = 16)
mpl.rc('ytick', labelsize = 16)
fig, ax = plt.subplots(2)
fig.suptitle(rf"Evolution of $\rho$, arbitrarily chosen $\Omega = {O}$ and $\Delta = {d}$", fontsize = 18)
ax[0].plot(x, 1-fun(x), label = r"$a\rightarrow$ probability of being in $|0\rangle$")
ax[0].plot(x, fun(x), label = r"$c\rightarrow$ probability of being in $|1\rangle$")
ax[0].legend(loc = 'best')
ax[1].set_xlabel("time", fontsize = 16)
ax[1].plot(x, re(x), label = r"Re$(b)$")
ax[1].plot(x, im(x), label = r"Im$(b)$")
ax[1].legend(loc = 'best')
plt.show()