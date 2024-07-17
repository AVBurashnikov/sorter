import unittest
from sorter import Sorter

class TestSorter(unittest.TestCase):

    def test_sort(self):
        bubble = Sorter("bubble")
        self.assertEqual(bubble.sort([3, 1, 2]), [1, 2, 3])
        select = Sorter("selection")
        self.assertEqual(select.sort([3, 1, 2]), [1, 2, 3])

    def test_sort_reverse(self):
        bubble = Sorter("bubble")
        self.assertEqual(bubble.sort_reverse([3, 1, 2]), [3, 2, 1])
        select = Sorter("selection")
        self.assertEqual(select.sort_reverse([3, 1, 2]), [3, 2, 1])
            

if __name__ == "__main__":
    unittest.main()