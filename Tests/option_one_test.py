import unittest
import assignment_six

class MyTestCase(unittest.TestCase):

    def test_is_duplicates(self):
        list_one = [1, 2, 3, 4, 4, 5, 6, 7, 8]
        list_two = [1, 1, 2, 3, 4, 5, 6, 7]
        list_three = [4, 5, 6, 7, 8, 8]
        list_four = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list_five = [1, 2, 3, 4, 5, 6, 7, -9, 9, 10]
        # self.assertTrue(assignment_six.is_duplicates(list_one))
        # self.assertTrue(assignment_six.is_duplicates(list_two))
        # self.assertTrue(assignment_six.is_duplicates(list_three))
        # self.assertFalse(assignment_six.is_duplicates(list_four))
        # self.assertFalse(assignment_six.is_duplicates(list_five))


if __name__ == '__main__':
    unittest.main()
