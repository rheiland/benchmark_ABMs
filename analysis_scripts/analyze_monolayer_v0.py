# Copy this script and pyMCDS.py into the output directory (/output_unit_test1)
#
# e.g.:
# python analyze_monolayer.py 330 331
#
__author__ = "Randy Heiland"

import sys,pathlib
#import xml.etree.ElementTree as ET
#import math
# import scipy.io
from pyMCDS import pyMCDS
#import matplotlib
#import numpy as np
import matplotlib.pyplot as plt

print(len(sys.argv))
if (len(sys.argv) < 4):
    print("--- No args provided, will try to use 'output' dir and 0th output file")  
    out_dir = "output"
    idx_min = 0
    idx_max = 1
else:
    kdx = 1
    out_dir = sys.argv[kdx]
    print("out_dir=",out_dir)
    kdx += 1
    idx_min = int(sys.argv[kdx])
    kdx += 1
    idx_max = int(sys.argv[kdx])

# print('frame, field = ',frame_idx, field_index)

t=[]
tumor_radius=[]
for idx in range(idx_min,idx_max):
    xml_file = "output%08d.xml" % idx

    # mcds = pyMCDS(xml_file, '../PhysiCell/output_usecase0')   # reads BOTH cells and substrates info
    mcds = pyMCDS(xml_file, out_dir)   # reads BOTH cells and substrates info
    # cell_ids = mcds.data['discrete_cells']['ID']
    cells_x = mcds.data['discrete_cells']['position_x']

    current_time = mcds.get_time()
    print('time (min)= ', current_time )
    print("# cells= ",cells_x.shape[0])
    print("monolayer diam= ",cells_x.max() - cells_x.min())

    t.append(current_time)
    # sub_intern.append(sintern)
    # sub_conc.append(sconc)

fig, ax = plt.subplots()
# ax.plot(t, sub_intern)
ax.set(xlabel='t', ylabel='monolayer radius')
# ax.title("cell's internal oxygen over time")
#ax.plot(t, sub_conc)
#ax.set(xlabel='t', ylabel='voxel(0,0,0) conc')
# ax.grid()
# fig.savefig("test.png")
# plt.show()
