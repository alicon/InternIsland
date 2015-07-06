from __future__ import division
import random
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
from collections import defaultdict
from colors import red,blue,green,black,yellow,magenta,cyan
import math
__author__ = 'samanthajohnson'

def addError(error_seq_string,base,is_error=False):
    """Either changes the base to be an error or not if is_error is false and adds it to the error sequence (in red)
    >>> addError('','G',False)
    'G'
    >>> addError('A','A',False)
    'AA'
    """
    """Either adds the unchanged base to the error string or chooses a random base to add depending on is_error

    :param str error_seq_string:
    :param str base: the current base in the sequence, either remains unchanged or gets changed to a random other base
    :param boolean is_error: defaults false, if true, adds a random base to the error_seq_string, else adds base
    :return: str error_seq_string: modified error sequence
    """
    if is_error:
        #There's an error! Pick a base from a set of three not including the base that needs to change
        error_base = 'AGCTAG'
        error_base_index = random.randint(0,2)
        if base == 'T':
            #Add the new, error base to the error string out of the first set
            error_seq_string += red(error_base[error_base_index],style = 'bold')
        elif base == 'A':
            #The '+ 1' is checking the second set of three bases
            error_seq_string += red(error_base[error_base_index + 1],style = 'bold')
        elif base == 'G':
            error_seq_string += red(error_base[error_base_index + 2],style = 'bold')
        elif base == 'C':
            error_seq_string += red(error_base[error_base_index + 3],style = 'bold')
    else:
        error_seq_string += base
    return error_seq_string

def printErrors(seq_name,seq_string,error_seq_string,error_num):
    """Prints all of the data nicely

    >>> printErrors('Seq1','ACGT','AGCT', 2)
    Seq1 no error:      ACGT
    Seq1 random errors: AGCT
    Number of random errors generated for Seq1: 2
    <BLANKLINE>

    """

    """Prints the original sequence, new error-filled sequence, sequence name, and number of errors in the new sequence

    :param str seq_name: Name of the sequence
    :param str seq_string: Un-tampered with sequence
    :param str error_seq_string: error sequence
    :param int error_num: number of errors generated in error sequence
    :return: void, just prints things out
    """
    print '{0} no error:      {1} \n' \
          '{0} random errors: {2} \n' \
          'Number of random errors generated for {0}: {3}'\
        .format(seq_name,seq_string,error_seq_string,error_num)

def createFastqDict(infile):
    """Creates a defaultdict of all the names of sequences as keys with their sequences as values given a fastq file

    :param str infile: name of the file to be read in and made a dict of
    :return: defaultdict sequences: the dictionary with the names and sequences
    """
    #infile = open(infile,'r')
    sequences = defaultdict(str)
    for line in infile:
        line = line.rstrip()
        if line[0] == '@':
            #Creates a key in the dictionary of the name of the sequence and sets the value to the sequence
            sequences[line[1:].rstrip()] = next(infile).rstrip()
    return sequences

def parse_cmdline_params(arg_list=None):
    """Parses command line arguments.
    :param arg_list: arguments from the command line
    :type arg_list: list
    :return: dictionary of options
    """

    description = "Calculate the GC percentage of sequences in a fasta file"
    parser = ArgumentParser(description=description,
                            formatter_class=ArgumentDefaultsHelpFormatter)

    parser.add_argument("--fastq", "-f", help="FASTQ file to process", required=True, type=FileType('r'))

    # Parse options
    opts = parser.parse_args(args=arg_list)
    return opts

def createQualityScores(sequence):
    """Makes a string of ascii characters corresponding to different quality values.

    :param str sequence: sequence to be translated
    :return: str new_ascii: ascii characters corresponding to the quality values determined by the error probability
    """
    ascii_ref = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    position = 0
    new_ascii = ''
    for base in sequence:
        position += 1
        error_prob = position * 0.001
        quality_score = -10 * math.log10(error_prob)
        new_ascii += ascii_ref[int(quality_score)]
    return new_ascii

def main(args):
    opts = parse_cmdline_params(args[1:])
    sequences = createFastqDict(opts.fastq)
    #sequences = createFastqDict('sampleFastq')
    total_error_num = 0
    total_errors = 0
    total_lengths = 0
    for key in sequences:
        error_seq_string = ''
        seq_name = key
        seq_string = sequences[key]
        position = 0
        error_num = 0
        quality_string = createQualityScores(seq_string)
        for base in seq_string:
            if base not in 'AGCT':
                raise ValueError("This base,", base ,",is not an A, G, C, or T!")
            position += 1
            error_prob = 0.001 * position
            if error_prob * 100 <= 0:
                raise ValueError("The error probability must be greater than 0!")
            #Checks if it needs to add an error
            if (random.randint(1,1000) < (error_prob)*1000):
                error_seq_string = addError(error_seq_string,base,True)
                error_num += 1
            else:
                error_seq_string = addError(error_seq_string,base,False)
        total_errors += error_num
        total_error_num += 1
        error_perc = error_num/len(seq_string)
        total_lengths += len(seq_string)
        printErrors(blue(seq_name),seq_string,error_seq_string,green(str(error_num)))
        print 'The error percent for this sequence is:',yellow(str(error_perc*100)),'%'
        print 'The new quality string is:            ',quality_string,'\n'
    print 'The average number of errors generated was:',magenta(str(int(total_errors/total_error_num)))
    print 'The total error percentage is:',magenta(str(total_errors/total_lengths*100)),'%'


if __name__ == '__main__':
    #import doctest
    #doctest.testmod()
    main(argv)