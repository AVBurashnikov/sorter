from abc import ABCMeta, abstractmethod
from typing import Callable, Any, List

class SortingMethod(metaclass=ABCMeta):

    @abstractmethod
    def run(self, sequence: list, reversed: bool=False):
        pass

class Bubble(SortingMethod):

    def run(self, sequence: list, reversed: bool=False):
        has_permute: bool = True

        while has_permute:
            has_permute = False
            for i in range(len(sequence)-1):
                if sequence[i] > sequence[i+1]:
                    sequence[i], sequence[i+1] = sequence[i+1], sequence[i]
                    has_permute = True
                    continue
        return sequence if not reversed else sequence[::-1]


class Selection(SortingMethod):
    
    def run(self, sequence: list, reversed: bool=False):
        for i in range(len(sequence)-1):
            min = sequence[i]
            min_index = i
            for j in range(i+1, len(sequence)):
                if sequence[j] < min:
                    min = sequence[j]
                    min_index = j
            sequence[i], sequence[min_index] = sequence[min_index], sequence[i]
        
        return sequence if not reversed else sequence[::-1]


class Insertion(SortingMethod):

    def run(self, sequence: list, reversed: bool=False):
        pass