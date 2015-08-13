from __future__ import division
__author__ = 'PaulComeau'
debug_dict={'chr17_41234634': '^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^],^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,', 'chr17_41234637': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'chr17_41234636': 'GGGGGGGGGGGGGGGGG$GGG$G$GGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGG$GGGGGGGG$GGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGG$GGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGG.....................................................................................GGGGGGGGGGGGGGGG$G$GG.....................................................................'}
from collections import OrderedDict
from Small_AccurateError_Functions import name_stripper
from Small_AccurateError_Functions import mpileup_percent_correct
import random

def Simple_Percent_Puller(fastq_dict, num_needed):
    #TODO this is incomplete
    needed_range = range(1, num_needed+1)
    stripped_dict_count = 0
    strip_num=0
    base_location_chance = {}
    range_dict = {}
    percent_error_list = []
    stripped_dict = name_stripper(mpileup_percent_correct(fastq_dict))
    for num in stripped_dict:
        stripped_dict_count += 1
        range_dict[stripped_dict_count] = stripped_dict[num]
    for num in range_dict:
        strip_num += 1
        float_marker = float(strip_num/stripped_dict_count)
        base_location_chance[num] = float_marker
    base_location_chance_clone = base_location_chance
    for number in needed_range:
        for base in base_location_chance_clone:
            rand_float = float(random.random())
            if rand_float <= base_location_chance_clone[base]:
                percent_error_list.append(range_dict[base])
                base_location_chance_clone = base_location_chance
                break
    return percent_error_list


def old_percent_puller(fastq_dict, num_needed):
    """
Creates a dictionary for use of the error_producer to fit the error probability of a real fastq
    :param fastq_dict: a dictionary which uses the position of base pairs and it's assinged chance of being a correct base pair
    :param num_needed: the amount of error percentages needed
    :return: dictionary with an assigned intiger and a percentage chance for a base pair at a location to be correct or incorrect
    """
    needed_range = range(1, num_needed+1)
    range_dict = {}
    count = 1
    base_location_chance = {}
    percent_error_list = []
    stripped_dict = name_stripper(mpileup_percent_correct(fastq_dict))
    for num in stripped_dict:
        base_location_chance[count] = stripped_dict[num]
        count += 1
    for num in base_location_chance:
        if num in needed_range:
            range_dict[num] = base_location_chance[num]
            percent_error_list.append(range_dict[num])
    return percent_error_list