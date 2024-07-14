from typing import Callable, Any, List

class Sorter:

    def sort(self, 
             sequence: list, 
             condition: Callable[[Any, Any], bool]=(lambda a, b: a > b) , 
             method: str='bubble_sort', order: str="asc") -> list:
        
        if sequence is None or not sequence or not isinstance(sequence, list):
            raise ValueError('Sequence must be specified and has a list type.')
        
        try:
            return {
                "bubble_sort": self.__bubble_sort,
            }[method](sequence, condition, order)
        
        except KeyError:
            raise KeyError("Unknown sort method: '%s'." % method)

    def __bubble_sort(self, 
                      seq: list, 
                      condition: Callable[[Any, Any], bool], 
                      order: str) -> Callable:
        has_replacement: bool = True

        while has_replacement:
            has_replacement = False

            for i in range(len(seq)-1):
                if condition(seq[i], seq[i+1]):
                    seq[i], seq[i+1] = seq[i+1], seq[i]
                    has_replacement = True
                    continue
        
        return self.__ordering_sequence(seq, order)
    
    def __ordering_sequence(self, 
                            sequence: list, 
                            order: str) -> list:
        if order == "asc":
            return sequence
        if order == "desc":
            return sequence[::-1]
        else:
            raise ValueError("Unknown sort order: '%s'" % order)
    




