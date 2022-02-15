#!/usr/bin/env python
import os, yaml
#PYMOL
import __main__
__main__.pymol_argv = [ 'pymol', '-qc' ]
import pymol
pymol.finish_launching()
from pymol import cmd

data = {}
#1. coordinates and obtain angle
os.system('t2x -c > opt_geometry.xyz')

with open('DH_ids.yml', 'r') as input:
    wano_file = yaml.full_load(input)
    id_list = wano_file['id_list']

    #Pymol work
    cmd.load('opt_geometry.xyz', 'mymol')
    cmd.set("retain_order",1)
    AngleValue = cmd.get_dihedral("id " + str(id_list[0]), "id " + str(id_list[1]), "id " + str(id_list[2]), "id " + str(id_list[3]))
    cmd.quit()

    #2. obtain energy
    EnergyValue = round(float(os.popen("eiger | grep 'Total energy =' | awk '{print $7}'").read()), 0) # energy in eV
    data['Angle'] = AngleValue
    data['Energy'] = EnergyValue

#3. write yaml outputfile
with open('tm_results.yml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
