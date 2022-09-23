#!/usr/bin/env python3
# coding: utf-8
import glob, shutil
import os, sys, subprocess
import xml.etree.ElementTree as ET
from modules import multicellds
import numpy as np


def get_full_df(outpath, last_index = 0):

    if last_index != 0:
        index = 1
        while index <= int(last_index):
            outpath_ix = outpath + f"_{index}"
            sys.stdout.write(f"\nObtaining dataframe... from {outpath_ix}  \n")
            try:
                mcds = multicellds.MultiCellDS(output_folder=outpath_ix)
                mcds.full_cell_info_df(group_by_time=False)
                mcds.full_cell_info_df(group_by_time=True)
            except:
                pass
            

            index += 1
    if last_index == 0:
        sys.stdout.write("\nObtaining dataframe... \n")
        mcds = multicellds.MultiCellDS(output_folder=outpath)
        mcds.full_cell_info_df(group_by_time=False)
        # mcds.full_cell_info_df(group_by_time=True)

        sys.stdout.write("\nDataframe obtained!\n")

if __name__ == "__main__":
    output_path = sys.argv[1]
    last_index = sys.argv[2]
    last_index = 0

    get_full_df(output_path, last_index)