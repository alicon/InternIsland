from __future__ import print_function
__author__ = 'PaulComeau'
def line_saver(infile):
    """
    saves lines to construct a fastq format file from the results of the error seeder
    :param infile: the original insilico fastq
    :return: a dictionary of needed read names and corresponding lines
    """
    infile.seek(0)
    constructed_dict = {}
    for line in infile:
        line = line.rstrip()
        if '@' in line:
            name = line
        if '+' in line:
            filler = line
            phred_line = next(infile)
            constructed_dict[name] = filler, phred_line.rstrip()
    return constructed_dict

def fastq_constructor(error_file, contruction_dict):
    """
    creates the fastq based off of bin depths and errors
    :param error_file: the file with seeded errors
    :param contruction_dict: dict with needed lines for insilico files
    :return: a file with the data in fastq format
    """
    final_output = open('fastq_results.txt', 'w')
    error_save = {}
    error_save_list = []
    for line in error_file:
        error_line = line.strip()
        if 'with errors' in error_line:
            error_save[line[0:17]] = line[-151:].rstrip()
            error_save_list.append(line[0:17])
    for name in contruction_dict:
        dict_content = contruction_dict[name]
        re_name = name[1:18]
        if '@' in name:
            for key in error_save_list:
                if key[0:17] == re_name:
                    print (name, file=final_output)
                    print (error_save[re_name], file=final_output)
                    print (dict_content[0], file=final_output)
                    print (dict_content[1], file=final_output)