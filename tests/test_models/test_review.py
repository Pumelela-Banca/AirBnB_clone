#!/usr/bin/python3
"""
module with tests for review class
"""


import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    class with test for review
    """
    def test_print_format(self):
        """
        tests __str__ result
        """
        test1 = Review()
        self.assertEqual(str(test1) , f"[Review] ({test1.id}) {test1.__dict__}")


if __name__ == '__main__':
    unittest.main()
