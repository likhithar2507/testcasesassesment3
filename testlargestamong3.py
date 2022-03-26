import largestamong3
import unittest
class check_largest_3num(unittest.TestCase):
    def setUp(self):
        self.x = 19
        self.y = 15
        self.z = 10

    def tearDown(self):
        self.x = 0
        self.y = 0
        self.z = 0

    def test_largest_num(self):
        result=largestamong3.Largest_of_3num(self.x,self.y,self.z)
        self.assertEqual(self.x,result)

if __name__=="__main__":
    unittest.main()
