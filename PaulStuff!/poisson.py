__author__ = 'PaulComeau'
import numpy
def number_of_clones(mean):
    clone_number=numpy.random.poisson(mean,1)
    return clone_number