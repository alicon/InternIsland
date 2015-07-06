__author__ = 'samanthajohnson'
import argparse
from collections import defaultdict
def createDataDict(infile):
    data = defaultdict(list)
    bedfile = open(infile,'r')
    for line in bedfile.readlines():
            if line != '\n':
                linelist = line.split()
                chrom_name = linelist[0]
                chrom_start = int(linelist[1])
                chrom_end = int(linelist[2])
                bp_range = chrom_end-(chrom_start+1)
                data[chrom_name].append((chrom_start, chrom_end, bp_range))
    return data

def countBPNoOverlap(infile):
    data = createDataDict(infile)
    result = 0
    for i in range(0,len(data.values())):
        result += (data.values()[i][0][2])
    #print "The BED file you provided covered", result, "base pairs, not accounting for overlap."
    return result

def countBPOverlap(infile):
    data = createDataDict(infile)
    result = countBPNoOverlap(infile)
    for i in range(0, len(data.keys())):
        for j in range(1,len(data.keys())-1):
            point_1 = ''
            point_2 = ''
            A = data[data.keys()[i]][0][0]+1
            B = data[data.keys()[i]][0][1]
            C = data[data.keys()[(i+j)%len(data.keys())]][0][0]+1
            D = data[data.keys()[(i+j)%len(data.keys())]][0][1]
            print A,B,C,D
            if A >= C:
                point_1 = A
            else:
                point_1 = C
            if B >= D:
                point_2 = D
            else:
                point_2 = B
            #print point_1,point_2
            if point_1 <= point_2:
                result -= ((point_2+1)-point_1)
            print result
    #print "The BED file you provided covered",result,"base pairs, accounting for overlap."
    return result


def main():
    print "The BED file you provided covered",countBPNoOverlap('SampleBED.txt'), "base pairs, not accounting for overlap."
    print "The BED file you provided covered",countBPOverlap('SampleBED.txt'),"base pairs, accounting for overlap."
main()