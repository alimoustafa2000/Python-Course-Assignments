# import module
import unittest

# class creation
class MyTestCase (unittest.TestCase):

    def test_one (self):
        self.assertIn(10, [5, 7, 8, 10], "10 should be present")

    def test_two (self):
        self.assertIs(type(10), int, "The Type Of 10 Is Int")

    def test_three (self):
        self.assertTrue(100, "Number 100 Return True")

    def test_four (self):
        self.assertFalse([], "Empty List [] Return False")

    def test_five (self):
        self.assertGreaterEqual(100, 90, "Number 100 should be greater than or Or Equal 90")


if __name__ == "__main__":

    unittest.main()