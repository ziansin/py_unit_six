import unittest
import modifying_lists


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


if __name__ == '__main__':
    unittest.main()
