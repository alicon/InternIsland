__author__ = 'samanthajohnson'
import unittest
import FastqError8
import argparse

class fastqErrorTests(unittest.TestCase):
    def setUp(self):
        self.fastq_lines = """\
        @SEQ_ID
        GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT
        +
        !''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
        @SEQ_ID2
        CGTATCGATCGGATAGATCGATAGGGAAATCGCCCTATGACCCTAGAGATGAGAGCGATG
        +
        !''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65
        """.splitlines(True)

        self.fastq_dict = {'SEQ_ID':'GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT',
                           'SEQ_ID2':'CGTATCGATCGGATAGATCGATAGGGAAATCGCCCTATGACCCTAGAGATGAGAGCGATG'}
        self.error_dict = {'SEQ_ID':'GATTTGGGGTTCAAGTCGTAGTCGTAGTCTGACGTATGCTCTTTGTTCAACTCACAGTTT',
                           'SEQ_ID2':'CGTATCGGATCGATCGCGATCGATCGGATAGATCGATAGGGAAATCGCCCTATGACCCTA'}

    def test_is_error(self):
        temp_value_add_error = FastqError8.is_error('A','')
        self.assertIn(temp_value_add_error, ['G','C','T'])
        temp_value_add_error = FastqError8.is_error('C','')
        self.assertIn(temp_value_add_error, ['G','A','T'])
        temp_value_add_error = FastqError8.is_error('G','')
        self.assertIn(temp_value_add_error, ['C','A','T'])
        temp_value_add_error = FastqError8.is_error('T','')
        self.assertIn(temp_value_add_error, ['G','C','A'])

    def test_is_not_error(self):
        self.assertEqual(FastqError8.is_not_error('A',''), 'A')

    def test_decide_if_error(self):
        self.assertIsNotNone(FastqError8.decide_if_error(self.fastq_dict))

if __name__ == '__main__':
    unittest.main()