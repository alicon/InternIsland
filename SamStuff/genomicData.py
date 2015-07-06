from __future__ import division
from collections import defaultdict
__author__ = 'samanthajohnson'

def gcContent(chromosome):
    """Find the GC Percentage given a string chromosome

    >>> gcContent(1)
    Traceback (most recent call last):
        ...
    TypeError: Chromosome needs to be a string.
    >>> gcContent('AT')
    0.0
    >>> gcContent('GC')
    100.0
    >>> gcContent('AG')
    50.0
    >>> gcContent('')
    Traceback (most recent call last):
        ...
    ValueError: Chromosome has no length.
    """
    """Finds the percentage of Gs and Cs in a chromosome.

    :param str chromosome: string, containing a line from a chromosome
    :return: int gc_perc
    """
    if chromosome != str(chromosome):
        raise TypeError("Chromosome needs to be a string.")
    if len(chromosome) == 0:
        raise ValueError("Chromosome has no length.")
    gcCount = 0
    chromosome = chromosome.upper()
    gcCount = chromosome.count("G") + chromosome.count("C")
    gc_perc = (gcCount/len(chromosome))*100
    #print gc_perc
    return gc_perc

def countLength(infile):
    """Counts the length of each chromosome in a fasta file.

    Calculates then stores the name, length, and GC percentage (by calling on gcContent) of the chromosome in a dictionary, which gets printed out later on.

    :param infile: The name of the file to be read in
    :type infile: str
    :return: None
    """
    infile = open(infile,'r')
    fasta_storage = defaultdict(list)
    chr_length = 0
    chr_full = ''
    chr_name = ''
    for line in infile:
        # Makes sure that '\n' doesn't get added to the chr length
        line = line.rstrip()
        if line[0] == '>' and chr_full != '':
            fasta_storage[chr_name] = [chr_length, gcContent(chr_full)]
            chr_length = 0
            chr_full = ''
            chr_name = line[1:]
            #Use this to see progress:
            #print chr_name
        elif line[0] == '>':
            chr_name = line[1:]
            chr_length = 0
            chr_full = ''
            #See progress:
            #print chr_name
        else:
            chr_length += len(line)
            chr_full += line
            #print fasta_storage
    fasta_storage[chr_name] = [chr_length, gcContent(chr_full)]
    percent_sum = 0
    percent_num = 0
    print 'Chr Name','\t\t','Chr Length','\t\t','GC Percent'
    for key in fasta_storage.keys():
        print key,'\t\t',fasta_storage[key][0],'\t\t',fasta_storage[key][1],'%'
        percent_sum += fasta_storage[key][1]
        percent_num += 1
    print 'Average GC Percentage:',(percent_sum/percent_num),'%'


countLength('sampleFASTA')
# This takes awhile, so just be patient or use the two 'print chr_name's to see where it's at

if __name__ == "__main__":
    import doctest
    doctest.testmod()