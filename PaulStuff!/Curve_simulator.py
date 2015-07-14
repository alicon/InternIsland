__author__ = 'PaulComeau'
import numpy as np
from scipy.stats import mode
def meanfinder(array):
    num_total=0
    amount=0
    for number in array:
        num_total+=number
        amount+=1
    return num_total/amount
def median(array):
    return np.median(array)
def mode(array):
    return mode(array)