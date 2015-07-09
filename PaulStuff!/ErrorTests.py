__author__ = 'PaulComeau'
import unittest
from RandomErrorHype import phredvalues_version8
from RandomErrorHype import errorproducer
class RandomErrorTests(unittest.TestCase):
    """test for the RandomError Generator
    """
    def setUp(self):
        self.phredlines="""\
;;3;;;;;;;;;;;;7;;;;;;;88
""".splitlines(True)

        self.fastQ="""\
@NCYC361-11a03.q1k bases 1 to 1576
GCGTGCCCGAAAAAATGCTTTTGGAGCCGCGCGTGAAAT
+NCYC361-11a03.q1k bases 1 to 1576
!)))))****(((***%%((((*(((+,**(((+**+,-
""".splitlines(True)

    def test_PhredValueTest(self):
        """test which makes sure that the phredvalues funtion finds accurate total phred score counts
        """
        phredscore=0
        realscore=[6.197200000000001 ,0.08488999999999997]
        for line in self.phredlines:
            phredscore=phredvalues_version8(line)
        self.assertEqual(phredscore, realscore)
        #since the function is used in errorproducer, the absurdly high value of 6.197 is needed to match self.fastQ's phred score

    def test_ErrorProduce(self):
        """test that makes sure the errorproducer can produce lines different from the original dataset
        """
        samplefastQ=iter(self.fastQ)
        Newline=errorproducer(samplefastQ)
        self.assertNotEqual(Newline, self.fastQ)
        #uses very high phred score to make sure that errors are produced and the two datasets are not equal




if __name__=='__main__':
    unittest.main()