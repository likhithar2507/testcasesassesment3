import evenorodd
import unittest
class check_even_odd(unittest.TestCase):
    def setUp(self):
        self.x1 = 14
        self.x2 = 15


    def tearDown(self):
        self.x1 = 0
        self.x2 = 0

    def test_even(self):
        result=evenorodd.even_odd(self.x1)
        self.assertEqual("even",result)

    def test_odd(self):
        result=evenorodd.even_odd(self.x2)
        self.assertEqual("odd",result)

if __name__=="__main__":
    unittest.main()
