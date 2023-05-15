# Project 4 – Graduate Rate (2017-2018)
# Name: Francisco Guzman
# Instructor: Dr. S. Einakian
# Section: 05

# unittest cases for graduate rate will include here
import unittest
from graduate_funcs import *
class TestCases(unittest.TestCase):
    def test_read_file_1(self):
        create_files(create_division(read_file('graduate_tests.py')),create_graduate(read_file('graduate_tests.py')))
        pass

    def test_create_division_1(self):
        pass

    def test_create_graduate_1(self):
        pass

    def test_find_total_avg_all_divisions_1(self):
        pass

    def test_find_graduate_rate_major_1(self):
        pass




# Run the unit test.
if __name__ == '__main__':
    unittest.main()
