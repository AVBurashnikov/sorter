from methods import SortingMethod, Bubble, Selection, Insertion

class Sorter:

    def __init__(self, method="bubble"):
        if not isinstance(method, str) or not method:
            raise ValueError("The method name must be a string representing the name of the sort method")
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
                "insertion": Insertion()
            }[self.method]
        except:
            KeyError("Invalid method")
