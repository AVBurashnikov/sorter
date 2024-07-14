import unittest
from sorter import Sorter

class TestSorter(unittest.TestCase):

    def test_sort_asc(self):
        sorter = Sorter()
        self.assertEqual(sorter.sort([3, 1, 2]), [1, 2, 3])

    def test_sort_desc(self):
        sorter = Sorter()
        self.assertEqual(sorter.sort([3, 1, 2], order="desc"), [3, 2, 1])

    def test_sort_unknown_sort_method(self):
        sorter = Sorter()
        self.assertRaises(KeyError, sorter.sort, [3, 1, 2], method="unknown")

    def test_sort_unknown_order_value(self):
        sorter = Sorter()
        self.assertRaises(ValueError, sorter.sort, [1, 2, 3], order="des")

    def test_sort_wrong_condition(self):
        sorter = Sorter()
        self.assertRaises(TypeError, sorter.sort, [1, 2, 3], condition=lambda a: a)

    def test_sort_not_list(self):
        sorter = Sorter()
        self.assertRaises(ValueError, sorter.sort, {1, 2, 3})
        self.assertRaises(ValueError, sorter.sort, (3, 2, 1))
        self.assertRaises(ValueError, sorter.sort, "123")
        self.assertRaises(ValueError, sorter.sort, 123)

    def test_sort_different_value_types(self):
        sorter = Sorter()
        self.assertRaises(TypeError, sorter.sort, [1, 2, "3"])        

if __name__ == "__main__":
    unittest.main()