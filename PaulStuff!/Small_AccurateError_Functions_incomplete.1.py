from __future__ import division
__author__ = 'PaulComeau'
debug_dict={'chr17_41234634': 'GGGGGGGGGGGGGGGGG$GGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$G$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGG$GGGGGGAGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$G$GGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG', 'chr17_41234637': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAATAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA$AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA', 'chr17_41234636': 'GGGGGGGGGGGGGGGGG$GGG$G$GGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGG$GGGGGGGG$GGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGG$GGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGG$GG$GGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGC$G$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$G$GGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGG$GG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGG$GGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGG$GG$GGGGGG$GGGGG$GGGGGGGGGG$GGGGGGGGG$GGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGG$GGGGGGGGGGGGGGGGGGGGGGG'}
from collections import OrderedDict
def name_stripper(base_dict):
    stripped_dict={}
    for key in base_dict:
        if '_' not in key [-10:]:
            stripped_dict[key [-10:]]=base_dict[key]
            continue
        if '_' not in key [-9:]:
            stripped_dict[key [-9:]]=base_dict[key]
            continue
        if '_' not in key [-8:]:
            stripped_dict[key [-8:]]=base_dict[key]
            continue
        if '_' not in key [-7:]:
            stripped_dict[key [-7:]]=base_dict[key]
            continue
        if '_' not in key [-6:]:
            stripped_dict[key [-6:]]=base_dict[key]
            continue
        if '_' not in key [-5:]:
            stripped_dict[key [-5:]]=base_dict[key]
            continue
        if '_' not in key [-4:]:
            stripped_dict[key [-4:]]=base_dict[key]
            continue
        if '_' not in key [-3:]:
            stripped_dict[key [-3:]]=base_dict[key]
            continue
        if '_' not in key [-2:]:
            stripped_dict[key [-2:]]=base_dict[key]
            continue
        if '_' not in key [-1:]:
            stripped_dict[key [-1:]]=base_dict[key]
            continue
    return stripped_dict

def cycle_counter(base_dict):#dict must be ordered
    base_check=0
    last_base=0
    start_base=0
    cycle_check=0
    ordered_base_dict=OrderedDict(base_dict)
    cycle_dict={}
    for base in ordered_base_dict:
        print base
        if last_base!=int(base)-1:
            cycle_check+=1
            end_base=base
            cycle_dict[cycle_check]=start_base, end_base
            base_check=cycle_check*150
        if cycle_check==base_check/150:
            start_base=base
        base_check+=1
        if base_check==150:
            end_base=base
            cycle_check+=1
            cycle_dict[cycle_check]=start_base, end_base
        last_base=base
    return cycle_dict

def snip_excluder(base_dict):
    snip_excluded_dict={}
    for base in base_dict:
        if base_dict[base] <= float(.3):
            continue
        if base_dict[base] > float(.3):
            snip_excluded_dict[base]=base_dict[base]
    return snip_excluded_dict

def general_correct_percent(bases_dict_raw):
    base_dict={}
    raw_base_dict=bases_dict_raw
    for base_location in raw_base_dict:
        total_base=0
        a_count=0
        t_count=0
        c_count=0
        g_count=0
        for base in raw_base_dict[base_location]:
            total_base+=1
            if base=='A':
                a_count+=1
            if base=='T':
                t_count+=1
            if base=='C':
                c_count+=1
            if base=='G':
                g_count+=1
            if base=='a':
                a_count+=1
            if base=='t':
                t_count+=1
            if base=='c':
                c_count+=1
            if base=='g':
                g_count+=1
        if a_count>t_count:
            if a_count>c_count:
                if a_count>g_count:
                    correct_base='a'
                    correct_count=a_count
        if t_count>a_count:
            if t_count>c_count:
                if t_count>g_count:
                    correct_base='t'
                    correct_count=t_count
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
    raw_base_dict = bases_dict_raw
    for base_location in raw_base_dict:
        total_base = 0
        complex_base_dict = {}
        a_count = 0
        t_count = 0
        c_count = 0
        g_count = 0
        for base in raw_base_dict[base_location]:
            total_base += 1
            if base is 'a' or 'A':
                a_count += 1
            if base is 't' or 'T':
                t_count += 1
            if base is 'c' or 'C':
                c_count += 1
            if base is 'g' or 'G':
                g_count += 1
        a_count_chance = float(a_count/total_base)
        t_count_chance = float(t_count/total_base)
        g_count_chance = float(g_count/total_base)
        c_count_chance = float(c_count/total_base)
        complex_base_dict[base_location] = a_count_chance, t_count_chance, g_count_chance, c_count_chance
    return complex_base_dict

#def percent_puller(dict_with_percent):#use stuff from previous curve things

print cycle_counter(name_stripper(debug_dict))