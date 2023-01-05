import unittest
import algorithms


class MyTestCase(unittest.TestCase):

    """
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
    """
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
"""
    def test_merge_example(self):
        list_one = [3, 4, 7, 9]
        list_two = [1, 5, 8, 11]
        self.assertEqual([1, 3, 4, 5, 7, 8, 9, 11], algorithms.merge(list_one, list_two))

    def test_merge_not_overlapping1(self):
        list_one = [6, 8, 11, 20]
        list_two = [2, 3, 4, 5]
        self.assertEqual([2, 3, 4, 5, 6, 8, 11, 20], algorithms.merge(list_one, list_two))

    def test_merge_not_overlapping2(self):
        list_one = [50, 60 , 70, 80]
        list_two = [100, 110, 120, 130]
        self.assertEqual([50, 60, 70, 80, 100, 110, 120, 130], algorithms.merge(list_one, list_two))
"""
if __name__ == '__main__':
    unittest.main()
