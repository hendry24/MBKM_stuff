import numpy as np

import matplotlib.pyplot as plt
plt.style.use('./SciencePlots-APS.mplstyle')

########

name = "Silicon"
prefix = "si"

wmin = 0
wmax = 30

data_dir = "./data/"

########

fig, ax = plt.subplots(3, 2, figsize = (7, 7))

fig.suptitle(f"Dielectric Functions of {name}")

dat_re = np.loadtxt(data_dir + f"epsr_{prefix}.dat", unpack = True)
dat_im = np.loadtxt(data_dir + f"epsi_{prefix}.dat", unpack = True)

########

c = 299792458 # m/s
hbar = 6.582119569e-16 # eV.s

########

index_arr = ['xx', 'yy', 'zz']

w = dat_re[0]   # energy

l = [1,1,1]     # lattice parameter correction factor

for i in range(3):
        
        eps_1 = dat_re[i + 1]
        eps_2 = dat_im[i + 1]

        eps_max = np.max([eps_1, eps_2]) * 1.05
        eps_min = np.min([eps_1, eps_2]) * 1.05
        
        # Plot epsilon in first column
        
        axx = ax[i][0]

        axx.plot(w, eps_1, color = "b", lw = 1.5)
        
        axx.set_xlabel(r"$\mathrm{Photon\ Energy}\ (eV)$")
        axx.set_xlim(wmin, wmax)

        axx.set_ylabel(r"$\mathrm{Re}\left(\varepsilon_{%s}\right)$" %index_arr[i], color = 'b')
        axx.set_ylim(eps_min, eps_max)
        
        axx.tick_params(axis = 'y', labelcolor = "b")

        ##############

        axx = ax[i][0].twinx()

        axx.plot(w, eps_2, color = "r", lw = 1.5, ls = "--")

        axx.set_ylabel(r"$\mathrm{Im}\left(\varepsilon_{%s}\right)$" %index_arr[i], color = 'r')
        axx.set_ylim(eps_min, eps_max)

        axx.tick_params(axis = 'y', labelcolor = 'r')

        # Plot alpha in second column

        axx = ax[i][1]

        alpha = 2 * (w / hbar / c) * np.sqrt( \
                l[i] / 2 * (np.sqrt(eps_1 ** 2 + eps_2 ** 2) - eps_1) )

        axx.plot(w, alpha / 1e8, color = 'k', lw = 1.5)

        axx.set_xlabel(r"$\mathrm{Photon\ Energy}\ (eV)$")
        axx.set_xlim(wmin, wmax)

        axx.set_ylabel(r"$\alpha_{%s}\ \left(\times 10^8\ \mathrm{m}^{-1}\right)$" %index_arr[i])
        axx.set_ylim(0, None)

plt.tight_layout()
plt.savefig(f"./Dielectric Functions of {name}.png", dpi = 600)
plt.show()
