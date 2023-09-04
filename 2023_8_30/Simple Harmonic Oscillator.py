import qutip as qt
import numpy as np
import matplotlib.pyplot as plt

N = 5

# Call the annihilation operator
a = qt.destroy(N)

# Define commutator
def com(A, B):
    return A * B - B * A

# Define the operators q and p in terms of the ladder operators
q = 2 ** (-0.5) * (a.dag() + a)

p = 1j * 2 ** (-0.5) * (a.dag() - a)

# Get basis
n = 0   # Ground state corresponds to n = 0

psi = qt.basis(N, n)

# Calculate expectation values

exp_p = qt.expect(p, psi)           # Using the qutip built-in function

exp_p2 = psi.dag() * p ** 2 * psi   # Using matrix multiplication

exp_q = psi.dag() * q * psi

exp_q2 = psi.dag() * q ** 2 * psi

# Calculate variance

del_q = exp_q2 - exp_q ** 2

del_p = exp_p2 - exp_p ** 2

print(exp_p2)