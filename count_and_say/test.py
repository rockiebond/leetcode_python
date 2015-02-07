import unittest
from unittest_data_provider import data_provider
from count_and_say import Solution
class TestCountAndSay(unittest.TestCase):
    def setUp(self):
        self.solution=Solution()
    numbers = lambda: (
        ('1',1),
        ('11',2),
        ('21',3),
        ('1211',4),
        ('111221',5),
    )

    @data_provider(numbers)
    def testCountAndSay(self, expected,number):
        self.assertEquals(expected,self.solution.countAndSay(number))

if __name__ == '__main__':
    unittest.main()
