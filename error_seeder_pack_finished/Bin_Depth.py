__author__ = 'PaulComeau'
import numpy as np
import seaborn
import pandas as pd
from scipy import stats,integrate
import matplotlib.pyplot as plt
#a=open('sampleFastq.fastq','r')
def BinDepthArray(infile):
    """
    this function takes a fastQ file and finds the bin depths for all genes
    :param infile:FastQ file
    :return:array of bin depths
    """
    binlist = []
    for line in infile:
        if '@' in line.rstrip():
            if '_' not in line[-6:]:
                binlist.append(int(line[-6:]))
            elif '_' not in line[-5:]:
                binlist.append(int(line[-5:]))
            elif '_' not in line[-4:]:
                binlist.append(int(line[-4:]))
            elif '_' not in line[-3:]:
                binlist.append(int(line[-3:]))
            elif '_' not in line[-2:]:
                binlist.append(int(line[-2:]))
            elif '_' not in line[-1:]:
                binlist.append(int(line[-1:]))
            binarray = np.asarray(binlist)
    return binarray
def Array_Grapher(array):
    """
    Simply creates a histogram from the array when running from a shell
    :param array: an array from a numpy function
    :return:a histogram of the array
    """
    seaborn.distplot(array)
#dank=BinDepthArray(a)
#print dank
#Array_Grapher(dank)
