mpirun -np 6 pw.x <Si.scf.in >Si.scf.out
mpirun -np 6 pw.x <Si.nscf.in >Si.nscf.out
mpirun -np 6 epsilon.x <Si.epsilon.in >Si.epsilon.out
