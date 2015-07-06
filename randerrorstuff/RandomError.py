from __future__ import division
__author__ = 'PaulComeau'
import random
import argparse
from sys import argv
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, FileType

import doctest

newstring=""
FastQ=open('ABL1_E_r_001_116_R_0_GSP2_R2.fastq', 'r')
errorchance=0
placemark=0
Pscorelist=[]

def phredvalues_version8(line):
    Pscore=0
    for ASCII in line:
        if ASCII is '"':
            Pscore+=.79433
        if ASCII is '#':
            Pscore+=.63096
        if ASCII is '$':
            Pscore+=.50119
        if ASCII is '%':
            Pscore+=.39811
        if ASCII is '&':
            Pscore+=.31623
        if ASCII is "'":
            Pscore+=.25119
        if ASCII is '(':
            Pscore+=.19953
        if ASCII is ')':
            Pscore+=.15849
        if ASCII is '*':
            Pscore+=.12589
        if ASCII is '+':
            Pscore+=.10000
        if ASCII is ',':
            Pscore+=.07043
        if ASCII is '-':
            Pscore+=.06310
        if ASCII is '.':
            Pscore+=.05012
        if ASCII is '/':
            Pscore+=.03981
        if ASCII is '0':
            Pscore+=.03162
        if ASCII is '1':
            Pscore+=.02512
        if ASCII is '2':
            Pscore+=.01995
        if ASCII is '3':
            Pscore+=.01585
        if ASCII is '4':
            Pscore+=.01259
        if ASCII is '5':
            Pscore+=.01000
        if ASCII is '6':
            Pscore+=.00794
        if ASCII is '7':
            Pscore+=.00631
        if ASCII is '8':
            Pscore+=.00501
        if ASCII is '9':
            Pscore+=.00398
        if ASCII is ':':
            Pscore+=.00316
        if ASCII is ';':
            Pscore+=.00251
        if ASCII is '<':
            Pscore+=.00200
        if ASCII is '=':
            Pscore+=.00158
        if ASCII is '>':
            Pscore+=.00126
        if ASCII is '?':
            Pscore+=.00100
        if ASCII is '@':
            Pscore+=.00079
        if ASCII is 'A':
            Pscore+=.00063
        if ASCII is 'B':
            Pscore+=.00050
        if ASCII is 'C':
            Pscore+=.00040
        if ASCII is 'D':
            Pscore+=.00032
        if ASCII is 'E':
            Pscore+=.00025
        if ASCII is 'F':
            Pscore+=.00020
        if ASCII is 'G':
            Pscore+=.00016
        if ASCII is 'H':
            Pscore+=.00013
        if ASCII is 'I':
            Pscore+=.00010
        if ASCII is 'J':
            Pscore+=.00008
    Pscorelist.append(Pscore)
    return Pscorelist

def phredscore(fastq_fh):
    Pscorelist=[]
    for line in fastq_fh:
        if 'B' in line:
            Pscorelist=phredvalues_version8(line)
            return Pscorelist






def errorproducer(fastq_fh):
    errorcount=0
    totaltotalbase=0
    Pscoreplacemark=0
    dankhold=0
    Pscorelist=[]
    for line in fastq_fh:
        if dankhold==0:
            Pscorelist=phredscore(fastq_fh)
        dankhold=1
        totalbase=0
        placemark=0
        newstring=""
        line=line.rstrip()
        #getting rid of \'s
        if 'B' in line:
            continue
        if '@' in line:
            continue
        if '}' in line:
            continue
        if '+' in line:
            continue
        if '-' in line:
            continue
        if ';' in line:
            continue
        #really sloppily discounting any lines apart from those with basepairs
        totalbase=len(line)
        totaltotalbase+=totalbase
        Pscoreplacemark=1
        print Pscorelist
        for basepair in line:
            placemark+=1
            errorchance=Pscorelist[Pscoreplacemark-1]
            int(errorchance)
            genedice=random.random()
            #checks place in line then produces a random number based on it
            if genedice > errorchance:
                newstring+=basepair
                continue
                #if the number generated is higher than the produced error chance, the base pair is added to a new line
            else:
                errorcount+=1
                if basepair==('G'):
                    if genedice < errorchance/3:
                        newstring+='A'
                        continue
                    if genedice < 2*errorchance/3:
                       newstring+='C'
                       continue
                    if genedice <= errorchance:
                        newstring+='T'
                        continue
                if basepair==('C'):
                    if genedice < errorchance/3:
                        newstring+='G'
                        continue
                    if genedice < 2*errorchance/3:
                       newstring+='A'
                       continue
                    if genedice <= errorchance:
                        newstring+='T'
                        continue
                if basepair==('A'):
                    if genedice < errorchance/3:
                        newstring+='G'
                        continue
                    if genedice < 2*errorchance/3:
                        newstring+='C'
                        continue
                    if genedice <= errorchance:
                        newstring+='T'
                        continue
                if basepair==('T'):
                    if genedice < errorchance/3:
                        newstring+='A'
                        continue
                    if genedice < 2*errorchance/3:
                        newstring+='C'
                        continue
                    if genedice <= errorchance:
                        newstring+='G'
                        continue
                    #if the generated number is lower than the error chance, then a random base pair is put in its place on the list
        print newstring
        print errorcount, 'errors'
        print errorcount/totaltotalbase*100, 'percentage of errors'

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