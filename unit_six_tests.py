import unittest
import modifying_lists
import algorithms
import assignment_six

class MyTestCase(unittest.TestCase):

    def test_create_list_1(self):
        self.assertEqual([1, 2], modifying_lists.create_list(1, 2))

    def test_create_list_2(self):
        self.assertEqual([-10, -9, -8, -7, -6, -5, -4, -3, -2], modifying_lists.create_list(-10, -2))

    def test_find_odds_1(self):
        sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = [1, 3, 5, 7, 9]
        self.assertEqual(expected, modifying_lists.find_odds(sample))

    def test_find_odds_2(self):
        sample = [9, 8, 9, 9, 8, 8, 9, 8]
        expected = [9, 9, 9, 9]
        self.assertEqual(expected, modifying_lists.find_odds(sample))

    def test_remove_duplicates_1(self):
        sample = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected, modifying_lists.remove_duplicates(sample))

    def test_remove_duplicates_2(self):
        sample = ["Mac", "Windows", "iPad", "iPod", "Windows", "Mac"]
        expected = ["Mac", "Windows", "iPad", "iPod"]
        self.assertEqual(expected, modifying_lists.remove_duplicates(sample))

    def test_add_numbers_1(self):
        sample = [1, 2, 3, 4, 5, -5, -4, -3, -2, -1]
        self.assertEqual(0, algorithms.add_numbers(sample))

    def test_add_numbers_2(self):
        sample = [-8, -9, -10]
        self.assertEqual(-27, algorithms.add_numbers(sample))

    def test_add_numbers_3(self):
        sample = [11, 22, 33, 44]
        self.assertEqual(110, algorithms.add_numbers(sample))

    def test_get_max_1(self):
        sample = [-9, -32, -5, -205, -115]
        self.assertEqual(-5, algorithms.get_max(sample))

    def test_get_max_2(self):
        sample = [1, 11, 111, 1111, 11111]
        self.assertEqual(11111, algorithms.get_max(sample))

    def test_get_min_1(self):
        sample = [-9, -32, -5, -205, -115]
        self.assertEqual(-205, algorithms.get_min(sample))

    def test_get_min_2(self):
        sample = [1, 11, 111, 1111, 11111]
        self.assertEqual(1, algorithms.get_min(sample))

    # def test_is_duplicates(self):
    #     list_one = [1, 2, 3, 4, 4, 5, 6, 7, 8]
    #     list_two = [1, 1, 2, 3, 4, 5, 6, 7]
    #     list_three = [4, 5, 6, 7, 8, 8]
    #     list_four = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #     list_five = [1, 2, 3, 4, 5, 6, 7, -9, 9, 10]
    #     self.assertTrue(assignment_six.is_duplicates(list_one))
    #     self.assertTrue(assignment_six.is_duplicates(list_two))
    #     self.assertTrue(assignment_six.is_duplicates(list_three))
    #     self.assertFalse(assignment_six.is_duplicates(list_four))
    #     self.assertFalse(assignment_six.is_duplicates(list_five))


if __name__ == '__main__':
    unittest.main()
