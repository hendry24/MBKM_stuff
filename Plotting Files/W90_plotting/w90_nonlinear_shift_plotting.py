import numpy as np
import matplotlib.pyplot as plt

plt.style.use('sci.mplstyle')

def plotit(folder_dir, name, prefix, savefig):

    xyz = ["x", "y", "z"]
    index_arr = np.array([[a + b + c for b in xyz for c in xyz] for a in xyz])
    
    fig, ax = plt.subplots(9, 3, figsize = (12, 28))
    fig.suptitle(f"Nonlinear Shift of {name} \n Calculated with Wannier90", 
                 fontsize = 20)
    
    for i in range(3):
        for j in range(9):
            
            index = index_arr[i][j]
            
            file = f"{folder_dir}/{prefix}-sc_{index}.dat"
            w, val = np.loadtxt(file, unpack = True)
            
            p = ax[j][i]
            p.plot(w, val, color = "b", lw = 1.5)
            p.set_xlabel(r"$\hbar\omega\ (\mathrm{eV})$")
            p.set_xlim(0, np.max(w))
            p.set_ylabel(r"$\sigma^{%s}\ (\mathrm{A/v^2})$" %index, 
                         fontsize = 20)
            p.set_ylim(np.min(val) * 1.05, np.max(val) * 1.05)
            
    plt.tight_layout()
    if savefig:
        plt.savefig(f"W90_Nonlinear Shift of {name}.jpg", dpi = 600)
    plt.show()

########################################################################################

plotit(folder_dir = "./nonlinear-shift", 
       name = "GaAs", 
       prefix = "GaAs", 
       savefig = True)
