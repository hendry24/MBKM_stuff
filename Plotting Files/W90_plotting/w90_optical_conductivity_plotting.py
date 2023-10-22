import numpy as np
import matplotlib.pyplot as plt

plt.style.use('sci.mplstyle')

def plotit(folder_dir, name, prefix, savefig):

    xyz = ["x", "y", "z"]
    index_arr = [[a + b for b in xyz] for a in xyz]
    
    fig, ax = plt.subplots(3, 3, figsize = (20, 15))
    fig.suptitle(f"Optical Conductivity of {name} \n Calculated with Wannier90", 
                 fontsize = 20)
    
    for i in range(3):
        for j in range(3):
            
            index = index_arr[i][j]
            
            file = f"{folder_dir}/{prefix}-kubo_S_{index}.dat"
            w, re, im = np.loadtxt(file, unpack = True)
            
            p = ax[i][j]
            p.plot(w, re, color = "b", lw = 1.5)
            p.set_xlabel(r"$\hbar\omega\ (\mathrm{eV})$")
            p.set_xlim(0, np.max(w))
            p.set_ylabel(r"$\mathcal{Re}\left\{\sigma_{%s}\right\}\ (\mathrm{S/cm})$" %index, 
                         color = "b", fontsize = 20)
            p.set_ylim(np.min(re) * 1.05, np.max(re) * 1.05)
            p.tick_params(axis ="y", labelcolor = "b")
            
            p = p.twinx()
            p.plot(w, im, color = "r", lw = 1.5)
            p.set_ylabel(r"$\mathcal{Im}\left\{\sigma_{%s}\right\}\ (\mathrm{S/cm})$" %index, 
                         color = "r", fontsize = 20)
            p.set_ylim(np.min(im) * 1.05, np.max(im) * 1.05)
            p.tick_params(axis ="y", labelcolor = "r")
    
    plt.tight_layout()
    if savefig:
        plt.savefig(f"W90_Optical Conductivity of {name}.jpg", dpi = 600)
    plt.show()

########################################################################################

plotit(folder_dir = "./Optical Conductivity", 
       name = "Graphene", 
       prefix = "gr", 
       savefig = True)
