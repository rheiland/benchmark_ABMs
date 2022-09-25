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

# print(len(sys.argv))
# if (len(sys.argv) < 4):
#     print("--- No args provided, will try to use 'output' dir and 0th output file")  
#     out_dir = "output"
#     idx_min = 0
#     idx_max = 1
# else:
#     kdx = 1
#     out_dir = sys.argv[kdx]
#     print("out_dir=",out_dir)
#     kdx += 1
#     idx_min = int(sys.argv[kdx])
#     kdx += 1
#     idx_max = int(sys.argv[kdx])

# print('frame, field = ',frame_idx, field_index)

out_dir = "../PhysiCell/output_monolayer"
t=[]
tumor_diam=[]
# for idx in range(0,507, 5):
for idx in [336, 386, 408, 481, 506]:
    xml_file = "output%08d.xml" % idx

    # mcds = pyMCDS(xml_file, '../PhysiCell/output_usecase0')   # reads BOTH cells and substrates info
    mcds = pyMCDS(xml_file, out_dir)   # reads BOTH cells and substrates info
    # cell_ids = mcds.data['discrete_cells']['ID']
    cells_x = mcds.data['discrete_cells']['position_x']

    current_time = mcds.get_time()
    print('time (min)= ', current_time )
    print('time (hr)= ', current_time/60. )
    print('time (day)= ', current_time/1440. )
    print("# cells= ",cells_x.shape[0])
    diam = cells_x.max() - cells_x.min()
    print("monolayer diam= ",diam)

    t.append(current_time/1440.)
    tumor_diam.append(diam)
    # sub_intern.append(sintern)
    # sub_conc.append(sconc)

fig, ax = plt.subplots()
# ax.plot(t, sub_intern)
ax.set(xlabel='t', ylabel='monolayer radius')
# ax.title("cell's internal oxygen over time")
# ax.plot(t, tumor_diam,'ko-')
ax.plot(t, tumor_diam,'k.-')
ax.set(xlabel='t (min)', ylabel='diameter')
# ax.grid()
# fig.savefig("test.png")
plt.show()
