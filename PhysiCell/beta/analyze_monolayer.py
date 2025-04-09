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
# from pyMCDS import pyMCDS
from pyMCDS_cells import pyMCDS_cells
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
out_dir = "../PhysiCell/output_monolayer_final"
out_dir = "./output_monolayer_live_cycle"
out_dir = "./output_monolayer_live_cycle_stochastic"
out_dir = "./output_monolayer_Oct2024"
#out_dir = "../PhysiCell/output_monolayer_pressure_set_behavior"
out_dir = "./output_monolayer"
t=[]
num_cells=[]
tumor_diam=[]

fig, ax = plt.subplots()

# ------- 1st plot all computed values (at every 10 hours)
hr_delta = 20
hr_delta = 1
#hr_delta = 10
# for idx in range(0,648, hr_delta):
max_frame = 615
max_frame = 162
max_frame = 120
for idx in range(0,max_frame+1, hr_delta):
    xml_file = "output%08d.xml" % idx
    # print("xml_file= ",xml_file)

    # mcds = pyMCDS(xml_file, '../PhysiCell/output_usecase0')   # reads BOTH cells and substrates info
    try:
        # mcds = pyMCDS(xml_file, out_dir)   # reads BOTH cells and substrates info
        mcds = pyMCDS_cells(xml_file, out_dir)   # reads BOTH cells and substrates info
    except:
        break
    # cell_ids = mcds.data['discrete_cells']['ID']
    cells_x = mcds.data['discrete_cells']['position_x']

    current_time = mcds.get_time()
    # print('time (min)= ', current_time )
    # print('time (hr)= ', current_time/60. )
    # print('time (day)= ', current_time/1440. )
    # print("# cells= ",cells_x.shape[0])
    num_cells.append(cells_x.shape[0])
    diam = cells_x.max() - cells_x.min()
    # print("monolayer diam= ",diam)

    t.append(current_time/1440.)
    tumor_diam.append(diam)
    # sub_intern.append(sintern)
    # sub_conc.append(sconc)

# ax.plot(t, tumor_diam,'k-')
# ax.plot(t, tumor_diam, marker='x', linestyle='-', color='b')
ax.plot(t, tumor_diam, linestyle='-', color='b')
csv_file = "monolayer_t_diam.csv"
with open(csv_file, 'w') as f:
    for idx in range(len(t)):
        # f.write(f'{tv[idx]},{xv[idx]}\n')
        f.write(f'{t[idx]},{tumor_diam[idx]}\n')
f.close()
print("---> ",csv_file)

csv_file = "monolayer_t_numcells.csv"
with open(csv_file, 'w') as f:
    for idx in range(len(t)):
        # f.write(f'{tv[idx]},{xv[idx]}\n')
        f.write(f'{t[idx]},{num_cells[idx]}\n')
f.close()
print("---> ",csv_file)

t2 = []
tumor_diam_pts = []
add_points_flag = True
# ------- 2nd plot just the points from the table
if add_points_flag:
# for idx in [336, 386, 408, 481, 506, 646]:   # times (hours) from Bru table (last value ~27d)
# for idx in [336, 386, 408, 481, 506, 614]:   # last is ~25.6 days
#   for idx in [84, 96, 102,   120, 126, 153]:   # approx if save interval =4 hrs
  for idx in [28, 32, 34,     40, 42, 54]:   # approx if save interval =12 hrs
    xml_file = "output%08d.xml" % idx

    # mcds = pyMCDS(xml_file, '../PhysiCell/output_usecase0')   # reads BOTH cells and substrates info
    # mcds = pyMCDS(xml_file, out_dir)   # reads BOTH cells and substrates info
    mcds = pyMCDS_cells(xml_file, out_dir)   # reads BOTH cells and substrates info
    # cell_ids = mcds.data['discrete_cells']['ID']
    cells_x = mcds.data['discrete_cells']['position_x']

    current_time = mcds.get_time()
    # print('time (min)= ', current_time )
    print('time (hr)= ', current_time/60. )
    # print('time (day)= ', current_time/1440. )
    print("# cells= ",cells_x.shape[0])
    diam = cells_x.max() - cells_x.min()
    print("monolayer diam= ",diam)

    t2.append(current_time/1440.)
    tumor_diam_pts.append(diam)

if add_points_flag:
  ax.plot(t2, tumor_diam_pts,'ro')

ax.set(xlabel='t (day)', ylabel='diameter (micron)',title="monolayer growth")
# ax.set_xlim(14, 28)

# ax.grid()
# fig.savefig("test.png")
plt.show()
