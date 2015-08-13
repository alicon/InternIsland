from __future__ import division
__author__ = 'PaulComeau'
#debug_dict = {'chr17_41234634': '^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^],^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,^K,', 'chr17_41234637': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'chr17_41234636': 'GGGGGGGGGGGGGGGGG$GGG$G$GGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGG$GGGGGGGG$GGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGG$GGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGG$GG$GGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGC$G$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$G$GGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGG$GG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGG$GGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGG$GG$GGGGGG$GGGGG$GGGGGGGGGG$GGGGGGGGG$GGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGG'}
from collections import OrderedDict
def name_stripper(base_dict):
    """
    remakes the dictionary with the name stripped down to a number value
    :param base_dict:dictionary with chromosome name and base location as the key
    :return:dictionary with only a base location as the key
    """
    stripped_dict = {}
    for key in base_dict:
        if '_' not in key[-10:]:
            stripped_dict[int(key[-10:])] = base_dict[key]
            continue
        if '_' not in key[-9:]:
            stripped_dict[int(key[-9:])] = base_dict[key]
            continue
        if '_' not in key[-8:]:
            stripped_dict[int(key[-8:])] = base_dict[key]
            continue
        if '_' not in key[-7:]:
            stripped_dict[int(key[-7:])] = base_dict[key]
            continue
        if '_' not in key[-6:]:
            stripped_dict[int(key[-6:])] = base_dict[key]
            continue
        if '_' not in key[-5:]:
            stripped_dict[int(key[-5:])] = base_dict[key]
            continue
        if '_' not in key[-4:]:
            stripped_dict[int(key[-4:])] = base_dict[key]
            continue
        if '_' not in key[-3:]:
            stripped_dict[int(key[-3:])] = base_dict[key]
            continue
        if '_' not in key[-2:]:
            stripped_dict[int(key[-2:])] = base_dict[key]
            continue
        if '_' not in key[-1:]:
            stripped_dict[int(key[-1:])] = base_dict[key]
            continue
    return stripped_dict

def cycle_counter(base_dict):#dict must be ordered
    """
    counts cycles for every 150 base pairs
    :param base_dict:dictionary with base pair locations as the key
    :return:dict with cycle number as the key and the starting base and ending base
    """
    base_check = 0
    last_base = 0
    start_base = 0
    cycle_check = 0
    ordered_base_dict = OrderedDict(base_dict)
    cycle_dict = {}
    for base in ordered_base_dict:
        print base
        if last_base != int(base)-1:
            cycle_check += 1
            end_base = base
            cycle_dict[cycle_check] = start_base, end_base
            base_check = cycle_check*150
        if cycle_check == base_check/150:
            start_base = base
        base_check += 1
        if base_check == 150:
            end_base = base
            cycle_check += 1
            cycle_dict[cycle_check] = start_base, end_base
        last_base = base
    return cycle_dict

def snip_excluder(base_dict):
    """
    excludes snips/base pairs with under 30% chance of being correct
    :param base_dict:dictionary with the error chance assigned to the key
    :return:dictionary without base pair locations below 30% chance being correct
    """
    snip_excluded_dict = {}
    for base in base_dict:
        if base_dict[base] <= float(.3):
            continue
        if base_dict[base] > float(.3):
            snip_excluded_dict[base] = base_dict[base]
    return snip_excluded_dict

def general_correct_percent(bases_dict_raw):
    """
    creates the dictionary with error chances to use in error seeding
    :param bases_dict_raw:dictionary with pileup data assigned to base pair locations
    :return:dictionary with base pair locations and error chance assigned to it
    """
    base_dict = {}
    raw_base_dict = bases_dict_raw
    for base_location in raw_base_dict:
        total_base = 0
        a_count = 0
        t_count = 0
        c_count = 0
        g_count = 0
        for base in raw_base_dict[base_location]:
            total_base += 1
            if base == 'A':
                a_count += 1
            if base == 'T':
                t_count += 1
            if base == 'C':
                c_count += 1
            if base == 'G':
                g_count += 1
            if base == 'a':
                a_count += 1
            if base == 't':
                t_count += 1
            if base == 'c':
                c_count += 1
            if base == 'g':
                g_count += 1
        if a_count > t_count:
            if a_count > c_count:
                if a_count > g_count:
                    correct_base = 'a'
                    correct_count = a_count
        if t_count > a_count:
            if t_count > c_count:
                if t_count > g_count:
                    correct_base = 't'
                    correct_count = t_count
        if c_count > g_count:
            if c_count > t_count:
                if c_count > a_count:
                    correct_base = 'c'
                    correct_count = c_count
        if g_count > c_count:
            if g_count > a_count:
                if g_count > t_count:
                    correct_base = 'g'
                    correct_count = g_count
        percent_count = float(correct_count/total_base)
        base_dict[base_location] = percent_count
    return base_dict

def specifics_correct_percent(bases_dict_raw):
    """
    makes a dictionary which gives the chance of each base pair to appear at a position
    :param bases_dict_raw: a dictionary with the position as the key and the base pairs found as the assigned value
    :return: a dictionary with the position as the key and four assigned values which is the percentage chance for each base pair to occur
    in the sequence a, t, g, then c.
    """
    raw_base_dict = bases_dict_raw
    complex_base_dict = {}
    for base_location in raw_base_dict:
        total_base = 0
        a_count = 0
        t_count = 0
        c_count = 0
        g_count = 0
        for base in raw_base_dict[base_location]:
            total_base += 1
            if base is 'A':
                a_count += 1
            if base is 'T':
                t_count += 1
            if base is 'C':
                c_count += 1
            if base is 'G':
                g_count += 1
            if base is 'a':
                a_count += 1
            if base is 't':
                t_count += 1
            if base is 'c':
                c_count += 1
            if base is 'g':
                g_count += 1
        a_count_chance = float(a_count/total_base)
        t_count_chance = float(t_count/total_base)
        g_count_chance = float(g_count/total_base)
        c_count_chance = float(c_count/total_base)
        complex_base_dict[base_location] = a_count_chance, t_count_chance, g_count_chance, c_count_chance
    return complex_base_dict

def mpileup_percent_correct(bases_dict_raw):
    """
    creates a dictionary of the percentage chance of a base pair being correct from the mpileup format
    :param bases_dict_raw:dictionary with base pair location and raw mpileup data
    :return:dictionary with base pairn location and percentage chance of being correct
    """
    raw_base_dict = bases_dict_raw
    mpileup_correct_dict = {}
    for base_location in raw_base_dict:
        total_base = 0
        match_count = 0
        noread_count = 0
        incorrect_count = 0
        for base in raw_base_dict[base_location]:
            total_base += 1
            if base is ',':
                match_count += 1
            elif base is '.':
                match_count += 1
            elif base is '^':
                total_base -= 2
            elif base is '$':
                total_base -= 1
            else:
                incorrect_count += 1
        if incorrect_count is 0:
            correct_chance = 1
        else:
            correct_chance = float(match_count/(total_base-noread_count))
        mpileup_correct_dict[base_location] = correct_chance
    return snip_excluder(mpileup_correct_dict)