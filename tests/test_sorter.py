import unittest
from sorter import Sorter

class TestSorter(unittest.TestCase):

    def test_sorter_bubble(self):
        bubble = Sorter("bubble")
        self.assertEqual(bubble.sort([3, 1, 2]), [1, 2, 3])

    def test_sorter_selection(self):
        select = Sorter("selection")
        self.assertEqual(select.sort([3, 1, 2]), [1, 2, 3])
    
    def test_sorter_insertion(self):
        insert = Sorter("insertion")
        self.assertEqual(insert.sort([3, 1, 2]), [1, 2, 3])

    def test_sorter_heapsort(self):
        heapsort = Sorter("heapsort")
        self.assertEqual(heapsort.sort([3, 1, 2]), [1, 2, 3])

    def test_sorter_quicksort(self):
        quicksort = Sorter("quicksort")
        self.assertEqual(quicksort.sort([3, 1, 2]), [1, 2, 3])    

    def test_sorter_bubble_reverse(self):
        bubble = Sorter("bubble")
        self.assertEqual(bubble.sort_reverse([3, 1, 2]), [3, 2, 1])

    def test_sorter_selection_reverse(self):
        select = Sorter("selection")
        self.assertEqual(select.sort_reverse([3, 1, 2]), [3, 2, 1])

    def test_sorter_insertion_reverse(self):
        insert = Sorter("insertion")
        self.assertEqual(insert.sort_reverse([3, 1, 2]), [3, 2, 1])

    def test_sorter_heapsort_reverse(self):
        heapsort = Sorter("heapsort")
        self.assertEqual(heapsort.sort_reverse([3, 1, 2]), [3, 2, 1])

    def test_sorter_heapsort_reverse(self):
        quicksort = Sorter("quicksort")
        self.assertEqual(quicksort.sort_reverse([3, 1, 2]), [3, 2, 1])
            
    def test_sorter_unknown_method(self):
        bubble = Sorter("buble")
        self.assertRaises(KeyError, bubble.sort, [3, 1, 2])


if __name__ == "__main__":
    unittest.main()