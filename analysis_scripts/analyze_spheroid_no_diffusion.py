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

out_dir = "../PhysiCell/output_usecase1"
t=[]
live_cells=[]

fig, ax = plt.subplots()

# live_cells = np.array( [(np.count_nonzero((mcds[idx].data['discrete_cells']['cell_type'] == 1) & (mcds[idx].data['discrete_cells']['cycle_model'] < 100) == True)) for idx in range(ds_count)] )

for idx in range(0,193):
    xml_file = "output%08d.xml" % idx

    # mcds = pyMCDS(xml_file, '../PhysiCell/output_usecase0')   # reads BOTH cells and substrates info
    mcds = pyMCDS(xml_file, out_dir)   # reads BOTH cells and substrates info

    cell_ids = mcds.data['discrete_cells']['ID']
    live = mcds.data['discrete_cells']['cycle_model'] < 100
    num_live = live.shape[0]

    print("# cells, # live= ",cell_ids.shape[0], num_live)

    current_time = mcds.get_time()
    # print('time (min)= ', current_time )
    # print('time (hr)= ', current_time/60. )
    # print('time (day)= ', current_time/1440. )

    t.append(current_time/60.)
    live_cells.append(num_live)

ax.plot(t, live_cells,'k-')

ax.set(xlabel='t (hr)', ylabel='# live cells',title="spheroid no diffusion")
# ax.grid()
# fig.savefig("test.png")
plt.show()
