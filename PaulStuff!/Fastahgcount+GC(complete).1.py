from __future__ import division
__author__ = 'PaulComeau'


humangenome=open('hg19.fa','r')
total_length=0
GCtotal=0
subtotallength=0
GCchrom_count=0
chrom_list=[]
chrom_namecount=-2
#Setting variables used in program

def Percentage_and_Print():
    GCchrom_percentage=GCchrom_count/subtotallength*100
    print 'GC percentage'
    print  GCchrom_percentage
    print 'Total Base Pairs'
    print subtotallength
#function for printing length of the chromosome and calculaing then printing the GC content percentage

for line in humangenome:
    if '>' in line:
        chrom_namecount=chrom_namecount+1
        chrom_name=line[1:]
        chrom_list.append(chrom_name)
        #records name of chromosome to refer to later

        if subtotallength==0:
            continue

        print chrom_list[chrom_namecount]
        Percentage_and_Print()
        GCtotal+=GCchrom_count
        #finds GC content percentage and lists data gathered from chromosome and creates a total for all GC base pairs found

        subtotallength=0
        GCchrom_count=0
        continue
        #resets total length value for chromosome and the GC count value for chromosome

    if line=='/n':
        continue

    line_length=0+len(line)
    total_length=total_length+line_length-1
    subtotallength=subtotallength+line_length-1
    #finds length of chromosome and total basepairs for genome

    Gline_count=line.count('G')+line.count('g')
    Cline_count=line.count('C')+line.count('c')
    GCline_count=Gline_count+Cline_count
    GCchrom_count=GCchrom_count+GCline_count
    #finds GC count for chromome
GCtotal+=GCchrom_count
print chrom_list[chrom_namecount+1]
Percentage_and_Print()
print 'Grand Total'
print total_length
print 'Average GC Percentage'
ChromAverage=GCtotal/total_length*100
print ChromAverage
#Prints out totals and finds final percentage for last chromosome, the average percentage in the file, as well as the total length for the Genome