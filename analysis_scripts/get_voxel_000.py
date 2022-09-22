#
__author__ = "Randy Heiland"

import sys,pathlib
import xml.etree.ElementTree as ET
import math
# import scipy.io
#from pyMCDS import pyMCDS
from pyMCDS_new import pyMCDS
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
sub_dict = mcds.data['continuum_variables']['oxygen']
sub_concentration = sub_dict['data']
print("sub_concentration.shape= ",sub_concentration.shape)
xval = 0
vconc = mcds.get_concentrations_at(x=xval, y=0., z=0.)
print("x, conc= ",xval,vconc)
fig, ax = plt.subplots()
#ax.plot(x, c)
ax.set(xlabel='x', ylabel='conc',
       title='title')
ax.grid()
# fig.savefig("test.png")
#plt.show()
