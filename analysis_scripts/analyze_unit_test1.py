# Copy this script and pyMCDS.py into the output directory (/output_unit_test1)
#
# python analyze_unit_test1.py 0 25
#
# Try to achieve ~12044 particles of substrate (20 uM) per timestep (in this case, 60 min). 
# Slope=12037/60 ~=200
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
    # conc = mcds.get_concentrations('oxygen')
    conc = mcds.get_concentrations('oxygen',z_slice=0.0)
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
ax.plot(t, sub_intern)
ax.set(xlabel='t', ylabel='internal oxygen')
ax.set_title("cell's internal oxygen over time")
#ax.plot(t, sub_conc)
#ax.set(xlabel='t', ylabel='voxel(0,0,0) conc')
# ax.grid()
# fig.savefig("test.png")
plt.show()
