import qutip as qt
import matplotlib.pyplot as plt
import numpy as np
import time

go = time.time()

N = 20

a = qt.destroy(N)

alpha_lst = np.linspace(0, 1, 100)

X_1 = 0.5 * (a + a.dag())
X_2 = 0.5 / 1j * (a - a.dag())

fig, ax = plt.subplots(3)

for phi in np.linspace(0, np.pi/2, 3):
    var_1_lst = []
    var_2_lst = []
    for alpha in alpha_lst:
        psi = alpha * qt.basis(N, 0) + np.sqrt(1-alpha ** 2) * np.exp(1j * phi) * qt.basis(N, 1)

        exp_X_1 = qt.expect(X_1, psi)
        exp_X_2 = qt.expect(X_2, psi)
        exp_X_1_2 = qt.expect(X_1 ** 2, psi)
        exp_X_2_2 = qt.expect(X_2 ** 2, psi)

        var_1 = exp_X_1_2 - exp_X_1 ** 2
        var_2 = exp_X_2_2 - exp_X_2 ** 2

        var_1_lst.append(var_1)
        var_2_lst.append(var_2)
    
    var_1_lst = np.array(var_1_lst)
    var_2_lst = np.array(var_2_lst)

    ax[0].plot(alpha_lst, var_1_lst, label = f"$\phi = {phi}$")
    ax[1].plot(alpha_lst, var_2_lst, label = f"$\phi = {phi}$")
    ax[2].plot(alpha_lst, var_1_lst * var_2_lst, label = f"$\phi = {phi}$")

name = [r"$(\langle X_1 \rangle)^2$", r"$(\langle X_2 \rangle)^2$", \
        r"$(\langle X_1 \rangle)^2(\langle X_2 \rangle)^2$"] 
for i in range(3):
    ax[i].legend(loc = 'lower left')
    ax[i].set_ylabel(name[i])

ax[2].set_xlabel(r'$\alpha$')

stop = time.time()

print(f"waktu = {stop-go}")

plt.show()

