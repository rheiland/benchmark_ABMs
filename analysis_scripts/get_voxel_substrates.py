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
if (len(sys.argv) < 2):
  frame_idx = 0
else:
  kdx = 1
  frame_idx = int(sys.argv[kdx])
# print('frame, field = ',frame_idx, field_index)

xml_file = "output%08d.xml" % frame_idx
mcds = pyMCDS(xml_file, '.')   # will read in BOTH cells and substrates info
current_time = mcds.get_time()
ncells = len(mcds.data['discrete_cells']['ID'])
x0 = -390
x=[]
c=[]
for xval in range(x0,399,20):
    vconc = mcds.get_concentrations_at(x=xval, y=0., z=0.)
    print("x, conc= ",xval,vconc)
    x.append(xval)
    c.append(vconc[0])
print(x)
print(c)
fig, ax = plt.subplots()
ax.plot(x, c)
ax.set(xlabel='x', ylabel='conc')
ax.grid()
# fig.savefig("test.png")
plt.show()
