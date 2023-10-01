import numpy as np
import matplotlib.pyplot as plt

def var_1(a,phi):
    return (3 - 2 * a ** 2) / 4 - a ** 2 * (1 - a ** 2) * np.cos(phi) ** 2

def var_2(a, phi):
    return (3 - 2 * a ** 2) / 4 - a ** 2 * (1 - a ** 2) * np.sin(phi) ** 2

a_lst = np.linspace(0, 1, 100)
phi_lst = np.linspace(0, np.pi/2, 5)

fig, ax = plt.subplots(3)
for phi in phi_lst:
    x1 = np.array([var_1(a, phi) for a in a_lst])
    x2 = np.array([var_2(a, phi) for a in a_lst])
    x1x2 = x1 * x2
    ax[0].plot(a_lst, x1, label = f"$\phi$ = {phi}")
    ax[1].plot(a_lst, x2, label = f"$\phi$ = {phi}")
    ax[2].plot(a_lst, x1x2, label = f"$\phi$ = {phi}")

ax[0].legend(loc = "lower left")
ax[1].legend(loc = "lower left")
ax[2].legend(loc = "lower left")
ax[0].axhline(0.25, linestyle = '--')
ax[1].axhline(0.25, linestyle = "--")
ax[2].axhline(1/16, linestyle = '--')
ax[0].set_ylabel(r"$(\Delta X_1)^2$")
ax[1].set_ylabel(r"$(\Delta X_2)^2$")
ax[2].set_ylabel(r"$(\Delta X_1)^2(\Delta X_2)^2$")
ax[2].set_xlabel(r"$\alpha$")

plt.show()