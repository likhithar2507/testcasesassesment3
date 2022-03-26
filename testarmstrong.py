import armstrong
import unittest

class check_armstromg_number(unittest.TestCase):
    def setUp(self):
        self.num1=153
        self.num2=154

    def tearDown(self):
        self.num1=0
        self.num2=0

    def test_armstrong(self):
        result=armstrong.armstrong_number(self.num1)
        self.assertEqual("Armstrong number",result)

    def test_not_armstrong(self):
        result=armstrong.armstrong_number(self.num2)
        self.assertEqual("not an Armstrong number",result)
if __name__=="__main__":
    unittest.main()