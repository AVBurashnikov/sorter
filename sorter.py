from methods import SortingMethod, Bubble, Selection

class Sorter:

    def __init__(self, method="bubble"):
        self.__sorter: SortingMethod = {
            "bubble": Bubble(),
            "selection": Selection(),
        }[method]       

    def sort(self, sequence) -> list:
        return self.__sorter.run(sequence)

    def sort_reverse(self, sequence) -> list:
        return self.__sorter.run(sequence, reversed=True)

    # def sort_with_condition(self, sequence, condition) -> list:
    #     pass

    # def sort_with_condition_reverse(self, sequence, condition) -> list:
    #     pass

     

    # def __bubble_sort(self, 
    #                   seq: list, 
    #                   condition: Callable[[Any, Any], bool], 
    #                   order: str) -> list:
    #     has_replacement: bool = True

    #     while has_replacement:
    #         has_replacement = False

    #         for i in range(len(seq)-1):
    #             if condition(seq[i], seq[i+1]):
    #                 seq[i], seq[i+1] = seq[i+1], seq[i]
    #                 has_replacement = True
    #                 continue
        
    #     return self.__ordering_sequence(seq, order)
    
    # def __merge_sort(self, 
    #                   seq: list, 
    #                   condition: Callable[[Any, Any], bool], 
    #                   order: str) -> list:
    #     raise NotImplementedError()

    # def __selection_sort(self, 
    #                   seq: list, 
    #                   condition: Callable[[Any, Any], bool], 
    #                   order: str) -> list:
    #     for i in range(len(seq)-1):
    #         min = seq[i]
    #         min_index = i
    #         for j in range(i+1, len(seq)):
    #             if condition(min, seq[j]):
    #                 min = seq[j]
    #                 min_index = j
    #         seq[i], seq[min_index] = seq[min_index], seq[i]
        
    #     return self.__ordering_sequence(seq, order)
 
    # def __ordering_sequence(self, 
    #                         sequence: list, 
    #                         order: str) -> list:
    #     if order == "asc":
    #         return sequence
    #     if order == "desc":
    #         return sequence[::-1]
    #     else:
    #         raise ValueError("Unknown sort order: '%s'" % order)

