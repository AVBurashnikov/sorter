from methods import SortingMethod, Bubble, Selection, Insertion, Heapsort, Quicksort

class Sorter:

    def __init__(self, method="bubble"):

        if not isinstance(method, str):
            raise TypeError("Sort method must be a string")
        
        if not method:
            raise ValueError("Sort method must be a non-empty string")

        self.method = method

    def sort(self, sequence) -> list:
        sorter = self.__get_sorter()
        return sorter.run(sequence)

    def sort_reverse(self, sequence) -> list:
        sorter = self.__get_sorter()
        return sorter.run(sequence, reversed=True)
    
    def __get_sorter(self) -> SortingMethod:
        try:
            return {
                "bubble": Bubble(),
                "selection": Selection(),
                "insertion": Insertion(),
                "heapsort": Heapsort(),
                "quicksort": Quicksort(),
            }[self.method]
        except:
            raise KeyError("Unknown method: '%s'" % self.method)
