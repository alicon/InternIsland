"""This program takes a fastq and adds errors

Run from terminal, must have ansicolors installed!
Found at: https://pypi.python.org/pypi/ansicolors/1.0.2

:return: None
"""
from __future__ import division

# Must install ansicolors module! Found at: https://pypi.python.org/pypi/ansicolors/1.0.2
__author__ = 'InternIsland'
from fastq_builder import fastq_constructor
from fastq_builder import line_saver
import numpy as np
import random
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
from collections import defaultdict
#from ansi_colors import blue, green, yellow
import os
from Accurate_ErrorChance_Puller import Simple_Percent_Puller
from Small_AccurateError_Functions import name_stripper
from Small_AccurateError_Functions import mpileup_percent_correct
from curvetesting2 import give_clone_list


def parse_cmdline_params(arg_list=None):
    """Parses command line arguments.

    :param arg_list: arguments from the command line
    :type arg_list: list
    :return: dictionary of options
    """

    description = "Add random errors to fastq sequences"
    parser = ArgumentParser(description=description,
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("--fastq", "-f",
                        help="FASTQ file to create a dist. from",
                        required=False,
                        default=open('60-0k_1_JH3968_S29_L001_R1_001.combined.molbar.trimmed.deduped.subset.fastq'),
                        type=FileType('r'))

    parser.add_argument("--cloning", "-c", choices=[0, 1, 2, 3], default=0,
                        help="Not required. "
                             "Pick 0 for no cloning."
                             "Pick 1 for poisson cloning. "
                             "Pick 2 for negative binomial cloning."
                             "Pick 3 for actual fastq distribution cloning.",
                        required=False,
                        type=int)

    parser.add_argument("--mean", "-m",
                        help="Not required unless cloning."
                             "The mean for poisson cloning.",
                        required=False,
                        type=float)

    parser.add_argument("--variance", "-v",
                        help="Required for neg. binomial."
                             "The variance or standard deviation for neg. binomial distribution.",
                        required=False,
                        type=float)

    parser.add_argument("--status_updates", "-s",
                        help="Enable status updates with True"
                             "The variance or standard deviation for neg. binomial distribution.",
                        default=False,
                        required=False,
                        type=bool)

    parser.add_argument("--insilico", "-i",
                        help="The file you actually want to run errors on",
                        required=False,
                        type=FileType('r'))

    parser.add_argument("--errors", "-e", choices=[0, 1], default=0,
                        help="Not required. "
                             "Pick 0 for linear error prob."
                             "Pick 1 for actual error prob",
                        required=False,
                        type=int)

    parser.add_argument("--pileup", "-p",
                        help="The file from the samtools pileup to find error prob",
                        required=False,
                        type=FileType('r'))


    opts = parser.parse_args(args=arg_list)
    #print opts
    return opts


def decide_if_error_1(fastq_dict, infile, status_updates, pileup_dict):
    """Decides if error, calls the corresponding function, creates a new dict with errors added

    :param defaultdict fastq_dict: the original, cloned (or not), dictionary
    :return defaultdict error_dict: the new dict with errors
    """
    error_dict = defaultdict()
    percent_list = Simple_Percent_Puller(pileup_dict, find_line_nums(infile, status_updates))
    infile.seek(0)
    for key in fastq_dict.keys():
        position = 0
        error_str = ''
        for base in fastq_dict[key]:
            error_prob = percent_list[position]
            position += 1
            if random.randint(1, 1000) > error_prob * 1000:
                error_str = is_error(base, error_str)
            else:
                error_str = is_not_error(base, error_str)
        error_dict[key] = error_str
    return error_dict

def decide_if_error_0(fastq_dict):
    """Decides if error, calls the corresponding function, creates a new dict with errors added
    :param defaultdict fastq_dict: the original, cloned (or not), dictionary
    :return defaultdict error_dict: the new dict with errors
    """
    error_dict = defaultdict()
    for key in fastq_dict.keys():
        position = 0
        error_str = ''
        for base in fastq_dict[key]:
            position += 1
            error_prob = position * .001
            if random.randint(1, 1000) < error_prob * 1000:
                error_str = is_error(base, error_str)
            else:
                error_str = is_not_error(base, error_str)
        error_dict[key] = error_str
    return error_dict


def is_error(base, error_str):
    """Adds a randomly decided base onto the current error string

    :param str base: the base to be 'replaced' in the new error string
    :param str error_str: the current error string to be added onto
    :return str error_str: the new error_str that had a base other than base added onto it
    """
    error_bases = 'AGCTAG'
    error_bases_ind = random.randint(0, 2)
    if base == 'T':
        error_str += error_bases[error_bases_ind]
    elif base == 'A':
        error_str += error_bases[error_bases_ind + 1]
    elif base == 'G':
        error_str += error_bases[error_bases_ind + 2]
    elif base == 'C':
        error_str += error_bases[error_bases_ind + 3]

    return error_str


def is_not_error(base, error_str):
    """Adds the base onto the error string

    :param str base: A single base to be added onto the error string
    :param str error_str: the current error string to have a base added onto it
    :return str error_str: returns the new error string after adding base
    """
    error_str += base
    return error_str


def poisson_clones(mean, line_num, status_updates):
    """Given the mean, finds number of times to clone the line using poisson dist.

    :param float mean: the mean of the data
    :param int line_num: the number of lines in the file
    :param bool status_updates: whether or not to print updates while running
    :return int: number of times to clone the line using poisson dist.
    """
    if status_updates:
        print "[STATUS] List created."
    return np.random.poisson(mean, line_num)


def nb_clones(mean, variance, line_num, status_updates):
    """Given mean and variance, gives the number of times to clone using n.b. distribution

    :param float mean: the mean of the data
    :param float variance: the standard deviation
    :param int line_num: the number of lines in the file
    :param bool status_updates: whether or not to print updates while running
    :return int: number of times to clone the line using neg. binomial distribution
    """
    if status_updates:
        print "[STATUS] List created."
    return np.random.negative_binomial(mean, variance, line_num)

def fastq_clones(status_updates, line_num, infile):
    """Finds the number of times to clone based on actual fastq dist.

    :param bool status_updates: whether or not to print updates while running
    :param int line_num: the number of lines in the file
    :return list data_list: the list of numbers selected from the file's distribution
    """
    data_list = give_clone_list(infile, line_num)
    if status_updates:
        print "[STATUS] List created."
    return data_list


def find_line_nums(insilico, status_updates):
    """Finds the number of lines in the file to be used later

    :param args opts: the user-inputted args parsed by argparse
    :return int line_num: the number of sequences in the file from opts
    """
    line_num = 0
    insilico.seek(0)
    for line in insilico:
        if '@' in line:
            line_num += 1
    if status_updates:
        print "[STATUS] Found number of lines."
    return line_num


def create_fastq_dict(infile, mean, variance, cloned, status_updates, fastq):
    """Creates a defaultdict from a fastq file with name and sequence and clones based on cloned

    Cloned defaults to 0 for no cloning, 1 for poisson, 2 for negative binomial, 3 for fastq dist.

    :param infile: the file to create the fastq from
    :param args opts: options parsed from command line
    :return: defaultdict of sequences and names
    """

    line_num = find_line_nums(infile, status_updates)
    infile.seek(0)

    if cloned == 1:
        clones = poisson_clones(mean, line_num, status_updates)
    elif cloned == 2:
        clones = nb_clones(mean, variance, line_num, status_updates)
    elif cloned == 3:
        clones = fastq_clones(status_updates, line_num, fastq)
    else:
        clones = [0] * line_num

    #print clones
    infile.seek(0)
    sequences = defaultdict(str)
    line_counter = 1
    for line in infile:
        line = line.rstrip()
        if line[0] == '@':
            next_line = next(infile).rstrip()
            sequences[line[1:].rstrip()] = next_line
            #print line_num
            #print clones[line_counter - 1]
            for clone_num in range(1, clones[line_counter - 1]):
                clone_num = str(clone_num)
                sequences[line[1:].rstrip() + ' (' + clone_num + ')'] = next_line
            #print sequences.keys()
            line_counter += 1
            if status_updates:
                print ("[STATUS] It's still going! {}".format(('.' * ((line_counter % 2) + 1))))
    if status_updates:
        print "[STATUS] Dictionary created."
    return sequences


def print_results(fastq_dict, error_dict):
    """Prints the contents of the original dictionary and the error dictionary

    :param defaultdict fastq_dict: dictionary with no errors
    :param defaultdict error_dict: dictionary with errors
    :return None: just prints
    """
    for key in fastq_dict.keys():
        print "{} no errors:    {}".format(key, fastq_dict[key])
        print "{} with errors:  {}\n".format(key, error_dict[key])


def write_results_to_file(fastq_dict, error_dict, opts):
    """Writes the result of the cloning/error adding to a file in the cwd

    :param defaultdict fastq_dict: original dictionary from file
    :param defaultdict error_dict: cloned/error dictionary
    :param args opts: the parsed arguments from the command line
    :return None: Writes to file only
    """
    outfile = open(opts.insilico.name[:-6] + '_FastqErrorResult.txt', 'w')
    for key in fastq_dict.keys():
        outfile.writelines("{} no errors:    {}\n".format(key, fastq_dict[key]))
        outfile.writelines("{} with errors:  {}\n\n".format(key, error_dict[key]))
    print ''\
               'Results written to {}'.format((''\
                '{}/{}_FastqErrorResult.txt'\
                '').format(os.getcwd(), opts.insilico.name[:-6]))


def create_samtools_dict(infile):
    """Creates a dictionary with the name_position as keys and string as value

    :param File infile: The file to be made into the dictionary
    :return defaultdict samtools_dict: Dictionary from the pileup file
    """
    samtools_dict = defaultdict()
    for line in infile:
        line_list = line.rsplit()
        chr_name = line_list[0] + '_' + line_list[1]
        chr_str = line_list[-2]
        samtools_dict[chr_name] = chr_str
    return samtools_dict


def main(args):
    """Main method

    :param args: arguments
    :return: None
    """
    print 'Running...'
    opts = parse_cmdline_params(args[1:])
    infile = opts.insilico
    mean = opts.mean
    variance = opts.variance
    status_updates = opts.status_updates
    cloning = opts.cloning
    fastq = opts.fastq
    pileup_file = opts.pileup
    errors = opts.errors
    if errors == 1:
        pileup_dict = create_samtools_dict(pileup_file)
    fastq_dict = create_fastq_dict(infile, mean, variance, cloning, status_updates, fastq)
    if errors == 1:
        error_dict = decide_if_error_1(fastq_dict, infile, status_updates, pileup_dict)
    elif errors == 0:
        error_dict = decide_if_error_0(fastq_dict)
    if status_updates:
        print "[STATUS] Error dict created."
    if raw_input('Would you like results printed to the terminal? Answer y or n: ') is 'y':
        print_results(fastq_dict, error_dict)
    if raw_input('Would you like to write the results to a file? Answer y or n: ') is 'y':
        write_results_to_file(fastq_dict, error_dict, opts)
        infile.seek(0)
        fastq_constructor(open(opts.insilico.name[:-6] + '_FastqErrorResult.txt', 'r'), line_saver(infile))
    print 'Done'


if __name__ == '__main__':
    main(argv)
