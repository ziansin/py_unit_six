import unittest
import intro_lists


class MyTestCase(unittest.TestCase):
    def test_swap_one(self):
        list1 = [12, 35, 9, 56, 24]
        expected = [24, 35, 9, 56, 12]
        self.assertEqual(expected,intro_lists.swap(list1))

    def test_swap_two(self):
        list1 = ["pie", "apple"]
        expected = ["apple", "pie"]
        self.assertEqual(expected,intro_lists.swap(list1))

    def test_rotate_left_one(self):
        list1 = [1, 2, 3]
        expected = [2, 3, 1]
        self.assertEqual(expected,intro_lists.rotate_left(list1))

    def test_rotate_left_two(self):
        list1 = [98, 99, -1]
        expected = [99, -1, 98]
        self.assertEqual(expected,intro_lists.rotate_left(list1))

    def test_rotate_left_three(self):
        list1 = [-4, -5, -6]
        expected = [-5, -6, -4]
        self.assertEqual(expected,intro_lists.rotate_left(list1))

    def test_max_end_one(self):
        list1 = [-4, -5, -6]
        expected = [-4, -4, -4]
        self.assertEqual(expected,intro_lists.max_end(list1))

    def test_max_end_two(self):
        list1 = [98, 99, -1]
        expected = [98, 98, 98]
        self.assertEqual(expected,intro_lists.max_end(list1))

    def test_max_end_three(self):
        list1 = [100, -9, 101]
        expected = [101, 101, 101]
        self.assertEqual(expected,intro_lists.max_end(list1))

if __name__ == '__main__':
    unittest.main()
