from __future__ import division
__author__ = "Paul Comeau"
import random
import time
start_time = time.time()
from Bin_Depth import BinDepthArray
from collections import OrderedDict
#a = open('60-0k_1_JH3968_S29_L001_R1_001.combined.molbar.trimmed.deduped.subset.fastq','r')

from collections import defaultdict
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
def array_range(data_array):
    """
    finds the range for a numbers in an array
    :param data_array: a data array
    :return: a range ,being the minimum occurring number in the array to the maximum
    """
    array_min = min(data_array)
    array_max = max(data_array)
    return range(array_min, array_max+1)


def array_counter(data_array):
    return data_array
def curve_simulator(fastq_file):
    """
    creates a dictionary which gives an approximation for the chance of all bin depths occurring in the range of occurring bin depths
    :param fastq_file:a FastQ file
    :return:dictionary with all bin depths and corresponding values
    """
    counted_depths = defaultdict(float)
    bin_array = BinDepthArray(fastq_file)
    fastq_range = array_range(bin_array)
    start_depth = 0
    for depth in bin_array:
        counted_depths[depth] += 1
    for depth in fastq_range:
        if depth in counted_depths:
            end_depth = depth
            if start_depth:
                distance = end_depth-start_depth
                if end_depth < start_depth:
                    occurence_differ = counted_depths[start_depth]-counted_depths[end_depth]
                if start_depth < end_depth:
                    occurence_differ = counted_depths[end_depth]-counted_depths[start_depth]
                if start_depth == end_depth:
                    occurence_differ = 0
                base_add = occurence_differ/distance
            temp_range = range(start_depth+1,end_depth+1)
            temp_check = start_depth
            if temp_check != 0:
                for depth in temp_range:
                    if depth not in counted_depths:
                        if start_depth < end_depth:
                            counted_depths[depth] = float(counted_depths[start_depth])+base_add
                        if start_depth > end_depth:
                            counted_depths[depth] = float(counted_depths[start_depth])-base_add
                        if start_depth == end_depth:
                            counted_depths[depth] = float(counted_depths[start_depth])
                        start_depth=depth
            start_depth = depth
    #print counted_depths
    return counted_depths

def percentage_finder(given_dict_raw):
    """
    uses dictionary to find the percentage chance for each bin depth to occur
    :param given_dict_raw: dictionary with predicted bin depth curve
    :return:dictionary with bin depths sorted to have compiled percentage values 0-1.00
    """
    bin_dictionary = given_dict_raw
    percent_dict = {}
    percent_compile_dict = {}
    bin_total = 0
    bin_percent_total = 0
    for key in bin_dictionary:
        bin_total += bin_dictionary[key]
    for key in bin_dictionary:
        percent_dict[key] = bin_dictionary[key]/bin_total
    for key in percent_dict:
        bin_percent_total += percent_dict[key]
        percent_compile_dict[key] = bin_percent_total
    #print percent_compile_dict
    return percent_compile_dict

def depth_selector(given_dict_percent, num_reads_to_model):
    """
    selects bin depth based on the percentage chance of it occurring
    :param given_dict_percent: dictionary from percentage_finder
    :param num_reads_to_model: an integer which represents the amount of bin depths to generate
    :return:
    """
    compiled_percentage_dict = OrderedDict(given_dict_percent)
    dict_dict = {}
    depth_list = []
    for number in range(0,num_reads_to_model):
        name = 'name',number
        fun = compiled_percentage_dict
        dict_dict[name] = fun
    for name in dict_dict:
        random_float = random.random()
        for key in dict_dict[name]:
            if random_float <= compiled_percentage_dict[key]:#radomfloat needs to be less than or equal to the percentage in the dict
                depth_list.append(key)
                break
    return depth_list
def parserthing(arglist=None):
    """
    gives arguments that allows for files to be opened by the program
    :param arglist: arguments from command line
    :return: options for the program/actions for it to take
    """
    description = 'generates random bin depths based on a fastq file'
    parser = ArgumentParser(description=description,
                           formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--fastq', '-f', help='put fastq here', required=True, type=FileType('r'))
    parser.add_argument('--num_depths', '-n', help='wanted number of bin depths', required=True, type=int)
    #command to open the named fastq file in read format
    options = parser.parse_args(args=arglist)
    return options

def give_clone_list(options, num_depths):
    clone_list = depth_selector(percentage_finder(curve_simulator(options.fastq)), num_depths)
    #print clone_list
    return clone_list

def main(args):
    """
    uses argurments from parserthing to find file that is used with errorproducer
    :param args: argument parsed from parserthing
    :return: running errorproducer with the given file
    """
    options = parserthing(args[1:])
    give_clone_list(options, 1)
    #runs the errorproduced with given file
    print ("--Curve Testing: %s seconds ---" % (time.time()-start_time))

if __name__ == '__main__':
    main(argv)


