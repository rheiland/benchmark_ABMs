# Examples (run from directory containing the .mat files):
#   - plot (time,xpos) of the right-most cell in the 11-cell mechanics test
#
#  At t=0, an immovable "wall" cell is at x=0 and the remaining 10 cells overlap by 1 radius width
#  so that the right-most cell (ID=10) is at x=50. We let the cells relax (adhesion=0; repulsion varies)
#  and plot the curve with the right-most cell reaches x=90.
#

import sys
import glob
import os
import xml.etree.ElementTree as ET
import math
from pathlib import Path

from pyMCDS import pyMCDS
try:
  import matplotlib
  from matplotlib import gridspec
  import matplotlib.colors as mplc
  from matplotlib.patches import Circle, Ellipse, Rectangle
  from matplotlib.collections import PatchCollection
except:
  print("\n---Error: cannot import matplotlib")
  print("---Try: python -m pip install matplotlib")
#  print("---Consider installing Anaconda's Python 3 distribution.\n")
  raise
try:
  import numpy as np  # if mpl was installed, numpy should have been too.
except:
  print("\n---Error: cannot import numpy")
  print("---Try: python -m pip install numpy\n")
  raise
from collections import deque
try:
  # apparently we need mpl's Qt backend to do keypresses 
  matplotlib.use("Qt5Agg")
#   matplotlib.use("TkAgg")
  import matplotlib.pyplot as plt
except:
  print("\n---Error: cannot use matplotlib's TkAgg backend")
#  print("Consider installing Anaconda's Python 3 distribution.")
  raise

# current_idx = 0
nargs = len(sys.argv)-1
print("# args=",nargs)
max_idx = 1
if nargs > 0:
    max_idx = int(sys.argv[1])
print("max_idx= ",max_idx)

#for idx in range(len(sys.argv)):
use_defaults = True
show_nucleus = 0
current_idx = 0
axes_min = 0.0
axes_max = 1000  

current_idx = 0
print("current_idx=",current_idx)

#d={}   # dictionary to hold all (x,y) positions of cells

""" 
--- for example ---
In [141]: d['cell1599'][0:3]
Out[141]: 
array([[ 4900.  ,  4900.  ],
       [ 4934.17,  4487.91],
       [ 4960.75,  4148.02]])
"""

# fig = plt.figure(figsize=(7,5))
fig = plt.figure(figsize=(5,5))  # square
ax0 = fig.gca()

tvals = []
xpos = []
#-----------------------------------------------------
def get_cells_xpos():
    global current_idx, axes_max,cax2,ax0,tvals,xpos

    frame = current_idx 

    xml_file_root = "output%08d.xml" % frame
    # print("------ plot_cells_xpos():  current_idx= ",current_idx)
    # print("xml_file_root = ",xml_file_root)
    # xml_file = os.path.join('.', xml_file_root)
    xml_file = os.path.join('output', xml_file_root)
    # print("xml_file= ",xml_file)

    if not Path(xml_file).is_file():
        print("ERROR: file not found",xml_file)
        return

    # mcds = pyMCDS(xml_file_root, microenv=False, graph=False, verbose=True)
    mcds = pyMCDS(xml_file, microenv=False, graph=False, verbose=False)
    total_min = mcds.get_time()  # warning: can return float that's epsilon from integer value
    # print("------ plot_cells_xpos():  total_min= ",total_min)
    try:
        df_all_cells = mcds.get_cell_df()
    except:
        print("plot_cells_xpos(): error performing mcds.get_cell_df()")
        sys.exit()
        # return
        
    xvals = df_all_cells['position_x']
    # print("type(xvals)= ",type(xvals))  # <class 'pandas.core.series.Series'>
    # print("xvals= ",xvals)

    # yvals = df_cells['position_y']

    # xpos.append(xvals/10)   # divide to get units of cell diam
    xpos.append(xvals)   # divide to get units of cell diam
    # print("xpos= ",xpos)
            

    axes_min = mcds.get_mesh()[0][0][0][0]
    axes_max = mcds.get_mesh()[0][0][-1][0]

    # title_str = '11 horizontal cells mechanics test (PhysiCell)'
    # ax0.set_title(title_str, fontsize=12)

print("\nNOTE: click in plot window to give it focus before using keys.")

# max_idx = 577
# max_idx = 5  # debugging
# max_idx = 106
print("\n------------------- 1st loop: get tvals ")
for idx in range(0,max_idx):
    xml_file_root = "output%08d.xml" % idx
    # print("---------- xml_file_root = ",xml_file_root)
    # xml_file = os.path.join('.', xml_file_root)
    xml_file = os.path.join('output', xml_file_root)
    # print("---------- xml_file= ",xml_file)
    # mcds = pyMCDS(xml_file_root, microenv=False, graph=False, verbose=True)
    mcds = pyMCDS(xml_file, microenv=False, graph=False, verbose=False)
    total_min = mcds.get_time()  # warning: can return float that's epsilon from integer value
    # print("total_min= ",total_min)
    tvals += [total_min]

print("\n------------------- 2nd loop: get xpos ")
for idx in range(0,max_idx):
    current_idx = idx
    get_cells_xpos()

# plt.plot(tvals,xpos,'o-', markersize=4)

# Scale so a time unit=1 represents 90% relaxation. This will become the cell cycle duration for the monolayer.
# t_90pct = 620.0
# t_90pct = 443.0
t_90pct = 1
tvals_ = np.array(tvals)   
xpos_ = np.array(xpos)   
len_tvals = len(tvals)
# print("len(tvals)=", len_tvals)
print("len(xpos)=",len(xpos))
# print("tvals_ =",tvals_)
# print("xpos_ =",xpos_)
# xpos_ = [[-2.5        -2.         -1.5        ...  1.5         2.
#    2.5       ]
#  [-2.80161294 -2.12722517 -1.54927079 ...  1.54927079  2.12722517
#    2.80161294]
#  [-2.98174944 -2.26149564 -1.63629156 ...  1.63629156  2.26149564
#    2.98174944]  ...
# plt.plot(tvals_/t_90pct, xpos,'-', markersize=4)
# plt.plot(tvals_/t_90pct, xpos,'-o', markersize=4)
tv = tvals_/t_90pct
# xv_start = xpos_[:,0]
# print("xv_start =",xv_start)
# xv_end = xpos_[:,10]
# print("xv_end =",xv_end)
cells_dist = xpos_[:,1] - xpos_[:,0]
with open("pc_plot_t_dist.csv", 'w') as f:
    for idx in range(len(tv)):
        f.write(f'{tv[idx]},{cells_dist[idx]}\n')
f.close()
# print("tissue_width =",tissue_width)
# plt.plot(tvals_/t_90pct, xpos_[:,10],'-', markersize=4)   # only plot the "last" curve (right-most cell)
# plt.plot(tvals_/t_90pct, tissue_width,'-', markersize=4)   # only plot the "last" curve (right-most cell)
plt.plot(tvals_, cells_dist,'-', markersize=4)   # only plot the "last" curve (right-most cell)

# ax0.set_xlim(0, 5)
ax0.set_ylim(0, 32)

# draw horiz and vertical dashed lines for rightmost cell reaching 90% relaxation width
# plt.plot([0,5],[9,9],'--k')
# plt.plot([1,1],[0,10],'--k')  # if scaled to "CD"
# plt.plot([0,5],[4.5,4.5],'--k')
# plt.plot([1,1],[2.5,5],'--k')  # if scaled to "CD"

# ax0.set_xlabel("Time (min)", fontsize=14)
ax0.set_xlabel("Time (min)", fontsize=12)

# ax0.set_ylabel("Cell center (microns)", fontsize=14)
# ax0.set_ylabel("Position (CD)", fontsize=14)
# ax0.set_ylabel("Tissue half-width (CD)", fontsize=14)
ax0.set_ylabel("Absolute distance of the centers of the cells", fontsize=10)

# title_str = '11 horizontal cells mechanics test (PhysiCell)'
# title_str = '11 horiz cells mechanics test (PhysiCell)'
# title_str = 'PhysiCell: relaxation test (10 cells)'
# title_str = 'PhysiCell: 11 compressed cells'
title_str = 'PhysiCell: 2 cells approaching (adhesion=2, repulsion=10)'
title_str = 'PhysiCell: 2 cells approaching (adhesion=4, repulsion=10)'
title_str = 'PhysiCell: 2 cells approaching (adhesion=0.4, repulsion=10)'
ax0.set_title(title_str, fontsize=10)

# keep last plot displayed
#plt.ioff()
# ax0.set_aspect('equal')
plt.show()
