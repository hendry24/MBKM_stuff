import qutip as qt
import matplotlib.pyplot as plt
import numpy as np

# Dimension
N = 15

# Annihilation operator
a = qt.destroy(N)

# Hamiltonian
omega = 1

H = omega * (a.dag() * a + 0.5)

# Initiate state
psi0 = qt.basis(N, 1)

# Make time list
timelst = np.linspace(0, 1, 100)

# Solve SE for states at time t
res_states = qt.sesolve(H, psi0, timelst).states

# Get expectation value of the number operator
exp_n = qt.expect(a.dag() * a, res_states)

print(exp_n)

plt.plot(exp_n)
plt.show()