# Dihedral-Scan
In this workflow, we use SimStack framework to perform dihedral scan calculations to determine global and local energy configuration with a molecule of interest.

### In this workflow, we will be able to:
```
1. Generate a molecule with SMILE code or use coordinates with PDB format.
2. Make a scan screening calculation of all possible dihedrals using SIMONA.
3. Obtain the coordinates for the best scored dihedral and the atom identity of the torsion.
4. With the support of Unpack and Range-It, we will Calculate the dihedral scan with DFT-Turbomole.
5. Obtain the dihedral profile using Table-Generator and Plot-Figure WaNos.
```


## Dihedral Scan workflow with **_Range-It_**

<img src="Figures/workflow.png"  width="50%">

**Fig 1** _Scheme of Dihedral-Scan workflow and the set up steps ._


## 1. Python Setup

To get this workflow up running on your available computational resources, make sure to have the below libraries installed on Python 3.6 or newer.

```
1. AmberTools and AcPype.
2. Gromacs.
3. Pymol (API).
4. Turbomole.
5. glob, tarfile, numpy, matplotlib, pandas.  
```

## 2. **_SIMONA-DHscan_** inputs

## 3. **_Unpack_** and for **_Range-it_** loop arrangement 

## 4. **_DFT-Turbomole_** inputs

## 5. **_Table-Generator_** inputs

## 6. **_Plot-Figure_** inputs
