import divisibleby5
import unittest
class check_disible_or_not(unittest.TestCase):
    def setUp(self):
        self.num1 = 15
        self.num2 = 11

    def tearDown(self):
        self.num1 = 0
        self.num2 = 0

    def test_divisible(self):
        result=divisibleby5.divisible(self.num1)
        self.assertTrue(result)

    def test_not_divisible(self):
        result=divisibleby5.divisible(self.num2)
        self.assertTrue(result)
if __name__=="__main__":
    unittest.main()