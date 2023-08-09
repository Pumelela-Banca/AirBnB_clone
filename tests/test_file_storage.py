#!/usr/bin/python3

"""
Tests file storage class and its instances
"""


import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    tests for storage methods
    """

    def test_all(self):
        """
        test cases for all method
        """
        # empty dictionary
        store = FileStorage()
        self.assertEquals(store.all(), {})



if __name__ == '__main__':
    unittest.main()
