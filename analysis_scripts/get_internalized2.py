#
# M1P~/git/tumor3D_ML/output$ python plot_substrate3D_slice.py 16 4
#
# Dependencies include matplotlib and numpy. We recommend installing the Anaconda Python3 distribution.
#
# Author: Randy Heiland (except for the circles() function)
#
#
__author__ = "Randy Heiland"

import sys,pathlib
import xml.etree.ElementTree as ET
import math
# import scipy.io
from pyMCDS import pyMCDS
import matplotlib
import numpy as np
from numpy.random import randn
import matplotlib.pyplot as plt

# print(len(sys.argv))
if (len(sys.argv) < 3):
  idx_min = 0
  idx_max = 10
else:
  kdx = 1
  idx_min = int(sys.argv[kdx])
  kdx += 1
  idx_max = int(sys.argv[kdx])

# print('frame, field = ',frame_idx, field_index)

t=[]
sub_intern=[]
sub_conc=[]
for idx in range(idx_min,idx_max):
    xml_file = "output%08d.xml" % idx
# print("plot_cells3D: xml_file = ",xml_file)
# mcds = pyMCDS_cells(xml_file, '.')  

# if not os.path.exists("tmpdir/" + xml_file):
# if not os.path.exists("output/" + xml_file):
    # return

# print("\n\n------------- plot_cells3D: pyMCDS reading info from ",xml_file)
# mcds = pyMCDS(xml_file, 'output')   # will read in BOTH cells and substrates info
    mcds = pyMCDS(xml_file, '.')   # will read in BOTH cells and substrates info
    current_time = mcds.get_time()
    # print('time=', current_time )
    # conc = mcds.get_concentrations('oxy')
    conc = mcds.get_concentrations('oxy',z_slice=0.0)
    # print('conc (z_slice=0)=',conc)

    sintern = mcds.data['discrete_cells']['internalized_total_substrates'][0]
    sconc = mcds.get_concentrations_at(x=0., y=0., z=0.)[0]
    sconc = mcds.get_concentrations_at(x=25., y=0., z=0.)[0]
    # sconc = mcds.get_concentrations_at(10., 10., 10.)[0]
    print("\nt= ",current_time,"  sintern= ",sintern,", sconc= ",sconc)
    # print("t, sintern, sconc= ",current_time,sconc)
    t.append(current_time)
    sub_intern.append(sintern)
    sub_conc.append(sconc)

fig, ax = plt.subplots()
#ax.plot(t, sub_intern)
#ax.set(xlabel='t', ylabel='internal')
ax.plot(t, sub_conc)
ax.set(xlabel='t', ylabel='voxel(0,0,0) conc')
# ax.grid()
# fig.savefig("test.png")
plt.show()
