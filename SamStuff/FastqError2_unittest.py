__author__ = 'samanthajohnson'
import unittest
import FastqError2
import tempfile

class addErrorTest(unittest.TestCase):

    def testaddError(self):
        self.assertEqual(FastqError2.addError('','G',False), 'G')
        self.assertEqual(FastqError2.addError('A','A',False),'AA')

if __name__ == "__main__":
    unittest.main()