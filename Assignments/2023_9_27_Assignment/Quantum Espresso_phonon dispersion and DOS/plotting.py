import numpy as np

import matplotlib.pyplot as plt
plt.style.use('./SciencePlots-APS.mplstyle')

########
data_dir = "./data/"

fig, ax = plt.subplots(1, 2, figsize = (9, 4.5), gridspec_kw = {'width_ratios' : [6, 3]})

fig.suptitle("Silicon")

########

phonon_dispersion_data = np.loadtxt(data_dir + "matdyn.freq.gp", unpack = True)

q = phonon_dispersion_data[0]

high_symmmetry_points = [q[0], q[30], q[60], q[-1]]
high_symmetry_labels = [r"L", r"$\Gamma$", r"X", r"L"]


for i in range(1, len(phonon_dispersion_data)):
    ax[0].plot(q, phonon_dispersion_data[i], color = "#007ba7", linewidth = 1.5)

ax[0].set_title("Phonon Dispersion")

ax[0].set_xticks(high_symmmetry_points)
ax[0].set_xticklabels(high_symmetry_labels)
ax[0].set_xlim(q[0], q[-1])

ax[0].set_ylabel(r"frequency ($cm^{-1}$)")
ax[0].set_ylim(0, None)

for x in high_symmmetry_points:
    ax[0].axvline(x = x, color = "#000000", linestyle = ":", linewidth = 1.0)

######

phonon_dos_data = np.loadtxt(data_dir + "si.phdos", unpack = True)

q = phonon_dos_data[0]

dos_labels = ["total", "s orbital", "p orbital"]
color_lst = ["red", "blue", "green"]

for i in range(1, len(phonon_dos_data)):
    ax[1].plot(phonon_dos_data[i], q, color = color_lst[i-1], linewidth = 1.5)
    ax[1].fill_betweenx(q, phonon_dos_data[i], color = color_lst[i-1], label = dos_labels[i-1])

ax[1].set_title("Phonon DOS")

ax[1].set_xlabel("DOS")
ax[1].set_xlim(0, None)

ax[1].set_ylabel(r"frequency ($cm^{-1}$)")
ax[1].set_ylim(q[0], q[-1])

ax[1].legend(loc = "best")

plt.tight_layout()
plt.savefig("./Band Structure and DOS of Silicon Phonon.png", dpi = 600)
plt.show()
