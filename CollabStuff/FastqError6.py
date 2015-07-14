"""This program takes a fastq and adds errors

Run from terminal, must have ansicolors installed! Found at: https://pypi.python.org/pypi/ansicolors/1.0.2

:return: None
"""
from __future__ import division

# Must install ansicolors module! Found at: https://pypi.python.org/pypi/ansicolors/1.0.2
__author__ = 'samanthajohnson'

import numpy
import random
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
from collections import defaultdict
from colors import red, blue, green, yellow, magenta
import math
import os


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
                        help="FASTQ file to process",
                        required=True,
                        type=FileType('r'))

    parser.add_argument("--cloning", "-c", choices=[0, 1, 2], default=0,
                        help="Not required. Pick 0 for no cloning.\n Pick 1 for poisson cloning.\n Pick 2 for negative binomial cloning.",
                        required=False,
                        type=int)

    parser.add_argument("--mean", "-m",
                        help="The mean for poisson cloning.",
                        required=False,
                        type=float)

    parser.add_argument("--variance", "-v",
                        help="The variance or standard deviation for negative binomial distribution.",
                        required=False,
                        type=float)
    opts = parser.parse_args(args=arg_list)
    return opts

def decide_if_error(fastq_dict):
    """Decides if error, calls the corresponding function, and creates a new dictionary with the errors added

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

def poisson_clones(mean):
    """Given the mean, finds number of times to clone the line using poisson dist.

    :param float mean: the mean of the data
    :return int: number of times to clone the line using poisson dist.
    """
    return numpy.random.poisson(mean, 1)


def nb_clones(mean, variance):
    """Given mean and variance, gives the number of times to clone using n.b. distribution

    :param float mean: the mean of the data
    :param float variance: the standard deviation
    :return int: number of times to clone the line using neg. binomial distribution
    """
    return numpy.random.negative_binomial(mean, variance)


def create_fastq_dict(infile, opts):
    """Creates a defaultdict from a fastq file with name and sequence and clones based on cloned

    Cloned defaults to 0 meaning no cloning, 1 means poisson, 2 means negative binomial

    :param infile: the file to create the fastq from
    :param args opts: options parsed from command line
    :return: defaultdict of sequences and names
    """
    cloned = opts.cloning

    if cloned == 1:
        n = poisson_clones(opts.mean)
    elif cloned == 2:
        n = nb_clones(opts.mean, opts.variance)
    else:
        n = 1
    sequences = defaultdict(str)
    for line in infile:
        line = line.rstrip()
        if line[0] == '@':
            next_line = next(infile).rstrip()
            sequences[line[1:].rstrip()] = next_line
            for x in range(0, n):
                sequences[line[1:].rstrip() + ' (' + str(x) + ')'] = next_line
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
    outfile = open(opts.fastq.name[:-6] + '_FastqErrorResult.txt', 'w')
    for key in fastq_dict.keys():
        outfile.writelines("{} no errors:    {}\n".format(key, fastq_dict[key]))
        outfile.writelines("{} with errors:  {}\n\n".format(key, error_dict[key]))
    print blue('Results written to {}'.format((os.getcwd() + '/' + opts.fastq.name[:-6] + '_FastqErrorResult.txt')))

def main(args):
    """Main method

    :param args: arguments
    :return: None
    """
    opts = parse_cmdline_params(args[1:])
    infile = opts.fastq
    fastq_dict = create_fastq_dict(infile, opts=opts)
    error_dict = decide_if_error(fastq_dict)
    print_results(fastq_dict, error_dict)
    write_results_to_file(fastq_dict, error_dict, opts)

if __name__ == '__main__':
    main(argv)
