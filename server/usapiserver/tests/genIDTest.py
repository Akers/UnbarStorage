
import usbase.models.operations as ops
import unittest

class GenerateIDTest(unittest.TestCase):
    def testArgs(self):
        c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
             'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
             'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
             'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '+', '-', ')', 'String']

        #when given len in int numbers
        for x in range(0, 101, 1):
            self.assertEqual(len(ops.generateID(x)), x)

        #when given len a number smaller than 0
        for x in range(-1, -101, -1):
            self.assertEqual(ops.generateID(x), -2)

        #when given len in chars or string
        for x in c:
            self.assertEqual(ops.generateID(x), -1)
