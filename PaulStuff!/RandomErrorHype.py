from __future__ import division
__author__ = 'PaulComeau'
import random
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
pscore_list = []

def phredvalues_version8(line):
    """ reads given line for ascii symbols and converts line to phred value
    :param line: a line with ascii characters that represents a phred value for base pairs
    :return: A list with the added total phred value for the line
    """
    ph_score = 0
    for ascii in line:
        if ascii is '"':
            ph_score += .79433
        if ascii is '#':
            ph_score += .63096
        if ascii is '$':
            ph_score += .50119
        if ascii is '%':
            ph_score += .39811
        if ascii is '&':
            ph_score += .31623
        if ascii is "'":
            ph_score += .25119
        if ascii is '(':
            ph_score += .19953
        if ascii is ')':
            ph_score += .15849
        if ascii is '*':
            ph_score += .12589
        if ascii is '+':
            ph_score += .10000
        if ascii is ',':
            ph_score += .07043
        if ascii is '-':
            ph_score += .06310
        if ascii is '.':
            ph_score += .05012
        if ascii is '/':
            ph_score += .03981
        if ascii is '0':
            ph_score += .03162
        if ascii is '1':
            ph_score += .02512
        if ascii is '2':
            ph_score += .01995
        if ascii is '3':
            ph_score += .01585
        if ascii is '4':
            ph_score += .01259
        if ascii is '5':
            ph_score += .01000
        if ascii is '6':
            ph_score += .00794
        if ascii is '7':
            ph_score += .00631
        if ascii is '8':
            ph_score += .00501
        if ascii is '9':
            ph_score += .00398
        if ascii is ':':
            ph_score += .00316
        if ascii is ';':
            ph_score += .00251
        if ascii is '<':
            ph_score += .00200
        if ascii is '=':
            ph_score += .00158
        if ascii is '>':
            ph_score += .00126
        if ascii is '?':
            ph_score += .00100
        if ascii is '@':
            ph_score += .00079
        if ascii is 'A':
            ph_score += .00063
        if ascii is 'B':
            ph_score += .00050
        if ascii is 'C':
            ph_score += .00040
        if ascii is 'D':
            ph_score += .00032
        if ascii is 'E':
            ph_score += .00025
        if ascii is 'F':
            ph_score += .00020
        if ascii is 'G':
            ph_score += .00016
        if ascii is 'H':
            ph_score += .00013
        if ascii is 'I':
            ph_score += .00010
        if ascii is 'J':
            ph_score += .00008
    pscore_list.append(ph_score)
    return pscore_list


def errorproducer(fastq_fh):
    """
    seeds in errors to base pairs according to a total phred score with corresponding phred line
    :param fastq_fh: the file handle/name
    :return:lines with errors seeded into them
    """

    error_count = 0
    total_total_base = 0
    pscore_placemark = 0
    pscore_list = []
    for line in fastq_fh:
        newstring = ""
        line = line.rstrip()
        #getting rid of \'s
        if 'B' in line:
            continue
        if '@' in line:
            continue
        if '}' in line:
            continue
        if 'G' in line:
            if 'T' in line:
                base_line = line
                line = next(fastq_fh)
        if '+' in line:
            phred_line = next(fastq_fh)
            pscore_list = phredvalues_version8(phred_line)
        #really baller way of ordering Basepair lines and finding Phredscore
        totalbase = len(base_line)
        total_total_base += totalbase
        pscore_placemark += 1
        for basepair in base_line:
            error_chance = pscore_list[pscore_placemark-1]
            int(error_chance)
            gene_dice = random.random()
            #checks place in line then produces a random number based on it
            if gene_dice > error_chance:
                newstring += basepair
                continue
                #number generated is higher than error chance base pair is added to a new line
            else:
                error_count += 1
                if basepair == 'G':
                    if gene_dice < error_chance/3:
                        newstring += 'A'
                        continue
                    if gene_dice < 2*error_chance/3:
                        newstring += 'C'
                        continue
                    if gene_dice <= error_chance:
                        newstring += 'T'
                        continue
                if basepair == 'C':
                    if gene_dice < error_chance/3:
                        newstring += 'G'
                        continue
                    if gene_dice < 2*error_chance/3:
                        newstring += 'A'
                        continue
                    if gene_dice <= error_chance:
                        newstring += 'T'
                        continue
                if basepair == 'A':
                    if gene_dice < error_chance/3:
                        newstring += 'G'
                        continue
                    if gene_dice < 2*error_chance/3:
                        newstring += 'C'
                        continue
                    if gene_dice <= error_chance:
                        newstring += 'T'
                        continue
                if basepair == 'T':
                    if gene_dice < error_chance/3:
                        newstring += 'A'
                        continue
                    if gene_dice < 2*error_chance/3:
                        newstring += 'C'
                        continue
                    if gene_dice <= error_chance:
                        newstring += 'G'
                        continue
                    #if the generated number is lower than the error chance random base pair is put in its place
        print newstring
        print error_count, 'errors'
        print error_count/total_total_base*100, 'percentage of errors'
    return newstring

def parserthing(arglist=None):
    """
    gives arguments that allows for files to be opened by the program
    :param arglist: arguments from command line
    :return: options for the program/actions for it to take
    """
    description = 'makes your files worse'
    parser = ArgumentParser(description=description,
                           formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--fastq', '-f', help='put fastq here', required=True, type=FileType('r'))
    #command to open the named fastq file in read format
    options = parser.parse_args(args=arglist)
    return options

def main(args):
    """
    uses argurments from parserthing to find file that is used with errorproducer
    :param args: argument parsed from parserthing
    :return: running errorproducer with the given file
    """
    options = parserthing(args[1:])
    errorproducer(options.fastq)
    #runs the errorproduced with given file







if __name__ == '__main__':
    main(argv)
