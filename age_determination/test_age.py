import unittest
from age import categorize_by_age

class TestAgeCategorization(unittest.TestCase):
    def test_child_age(self):
        self.assertEqual(categorize_by_age(5), "Child")
        self.assertEqual(categorize_by_age(9), "Child")
    def test_teenager_age(self):
        self.assertEqual(categorize_by_age(10), "Teenager")
        self.assertEqual(categorize_by_age(15), "Teenager")
        self.assertEqual(categorize_by_age(18), "Teenager")
    def test_adult_age(self):
        self.assertEqual(categorize_by_age(19), "Adult")
        self.assertEqual(categorize_by_age(30), "Adult")
        self.assertEqual(categorize_by_age(64), "Adult")
    def test_golden_age(self):
        self.assertEqual(categorize_by_age(65), "Golden Age")
        self.assertEqual(categorize_by_age(80), "Golden Age")
        self.assertEqual(categorize_by_age(120), "Golden Age")
    def test_invalid_age(self):
        self.assertEqual(categorize_by_age(-1), "Invalid Age: -1")
        self.assertEqual(categorize_by_age(121), "Invalid Age: 121")