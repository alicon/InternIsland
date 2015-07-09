from __future__ import division
__author__ = 'PaulComeau'
import random
import argparse
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType
Pscorelist=[]

def phredvalues_version8(line):
    """ reads given line for ASCII symbols and converts line to phred value
    :param line: a line with ASCII characters that represents a phred value for base pairs
    :return: A list with the added total phred value for the line
    """
    Ph_score=0
    for ASCII in line:
        if ASCII is '"':
            Ph_score+=.79433
        if ASCII is '#':
            Ph_score+=.63096
        if ASCII is '$':
            Ph_score+=.50119
        if ASCII is '%':
            Ph_score+=.39811
        if ASCII is '&':
            Ph_score+=.31623
        if ASCII is "'":
            Ph_score+=.25119
        if ASCII is '(':
            Ph_score+=.19953
        if ASCII is ')':
            Ph_score+=.15849
        if ASCII is '*':
            Ph_score+=.12589
        if ASCII is '+':
            Ph_score+=.10000
        if ASCII is ',':
            Ph_score+=.07043
        if ASCII is '-':
            Ph_score+=.06310
        if ASCII is '.':
            Ph_score+=.05012
        if ASCII is '/':
            Ph_score+=.03981
        if ASCII is '0':
            Ph_score+=.03162
        if ASCII is '1':
            Ph_score+=.02512
        if ASCII is '2':
            Ph_score+=.01995
        if ASCII is '3':
            Ph_score+=.01585
        if ASCII is '4':
            Ph_score+=.01259
        if ASCII is '5':
            Ph_score+=.01000
        if ASCII is '6':
            Ph_score+=.00794
        if ASCII is '7':
            Ph_score+=.00631
        if ASCII is '8':
            Ph_score+=.00501
        if ASCII is '9':
            Ph_score+=.00398
        if ASCII is ':':
            Ph_score+=.00316
        if ASCII is ';':
            Ph_score+=.00251
        if ASCII is '<':
            Ph_score+=.00200
        if ASCII is '=':
            Ph_score+=.00158
        if ASCII is '>':
            Ph_score+=.00126
        if ASCII is '?':
            Ph_score+=.00100
        if ASCII is '@':
            Ph_score+=.00079
        if ASCII is 'A':
            Ph_score+=.00063
        if ASCII is 'B':
            Ph_score+=.00050
        if ASCII is 'C':
            Ph_score+=.00040
        if ASCII is 'D':
            Ph_score+=.00032
        if ASCII is 'E':
            Ph_score+=.00025
        if ASCII is 'F':
            Ph_score+=.00020
        if ASCII is 'G':
            Ph_score+=.00016
        if ASCII is 'H':
            Ph_score+=.00013
        if ASCII is 'I':
            Ph_score+=.00010
        if ASCII is 'J':
            Ph_score+=.00008
    Pscorelist.append(Ph_score)
    return Pscorelist


def errorproducer(fastq_fh):
    """
    seeds in errors to base pairs according to a total phred score for the corresponding phred score line
    :param fastq_fh: the file handle/name
    :return:lines with errors seeded into them
    """

    error_count=0
    total_total_base=0
    Pscore_placemark=0
    Pscorelist=[]
    for line in fastq_fh:
        place_mark=0
        newstring=""
        line=line.rstrip()
        #getting rid of \'s
        if 'B' in line:
            continue
        if '@' in line:
            continue
        if '}' in line:
            continue
        if 'G' in line:
            if 'T' in line:
                BaseLine=line
                line=next(fastq_fh)
        if '+' in line:
            Phredline=next(fastq_fh)
            Pscorelist=phredvalues_version8(Phredline)
        #really baller way of ordering Basepair lines and finding Phredscore
        totalbase=len(BaseLine)
        total_total_base+=totalbase
        Pscore_placemark+=1
        for basepair in BaseLine:
            place_mark+=1
            error_chance=Pscorelist[Pscore_placemark-1]
            int(error_chance)
            gene_dice=random.random()
            #checks place in line then produces a random number based on it
            if gene_dice > error_chance:
                newstring+=basepair
                continue
                #if the number generated is higher than the produced error chance, the base pair is added to a new line
            else:
                error_count+=1
                if basepair==('G'):
                    if gene_dice < error_chance/3:
                        newstring+='A'
                        continue
                    if gene_dice < 2*error_chance/3:
                       newstring+='C'
                       continue
                    if gene_dice <= error_chance:
                        newstring+='T'
                        continue
                if basepair==('C'):
                    if gene_dice < error_chance/3:
                        newstring+='G'
                        continue
                    if gene_dice < 2*error_chance/3:
                       newstring+='A'
                       continue
                    if gene_dice <= error_chance:
                        newstring+='T'
                        continue
                if basepair==('A'):
                    if gene_dice < error_chance/3:
                        newstring+='G'
                        continue
                    if gene_dice < 2*error_chance/3:
                        newstring+='C'
                        continue
                    if gene_dice <= error_chance:
                        newstring+='T'
                        continue
                if basepair==('T'):
                    if gene_dice < error_chance/3:
                        newstring+='A'
                        continue
                    if gene_dice < 2*error_chance/3:
                        newstring+='C'
                        continue
                    if gene_dice <= error_chance:
                        newstring+='G'
                        continue
                    #if the generated number is lower than the error chance, then a random base pair is put in its place on the list
        print newstring
        print error_count, 'errors'
        print error_count/total_total_base*100, 'percentage of errors'
    return newstring

def parserthing(arglist=None):
    description='makes your files worse'
    parser=ArgumentParser(description=description,
                          formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument('--fastq','-f', help='put in fastq here', required=True, type=FileType('r'))
    #set up command to open the named fastq file in read format
    options = parser.parse_args(args=arglist)
    return options

def main(args):
    options=parserthing(args[1:])
    errorproducer(options.fastq)
    #runs the errorproduced with given file







if __name__ == '__main__':
    main(argv)