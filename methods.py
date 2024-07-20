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
        for i in range(1, len(sequence)):
            for j in range(i, 0, -1):
                if sequence[j] < sequence[j-1]:
                    sequence[j], sequence[j-1] = sequence[j-1], sequence[j]
        
        return sequence if not reversed else sequence[::-1]


class Heapsort(SortingMethod):

    def run(self, sequence: List, reversed: bool = False):
        heap_size = len(sequence)

        for i in range(heap_size):
            self.__build_heap(sequence, heap_size - i)
            sequence[-i], sequence[0] = sequence[0], sequence[-i]

        return sequence if not reversed else sequence[::-1]

    def __build_heap(self, s: List, heap_size: int):
        i = heap_size//2 - 1
        while i >= 0:
            if s[i] < s[2*i + 1]:
                s[i], s[2*i + 1] = s[2*i + 1], s[i]
            if i*2 + 2 < heap_size and s[i] < s[2*i + 2]:
                s[i], s[2*i + 2] = s[2*i + 2], s[i]
            i -= 1

class Quicksort(SortingMethod):

    def run(self, sequence: List, reversed: bool = False):
        
        def __recursively_sort(sequence):

            if len(sequence) <= 1:
                return sequence

            equal_base, less_than_base, greater_than_base = [], [], []

            for e in sequence:
                if sequence[0] == e:
                    equal_base.append(e)
                elif sequence[0] < e:
                    greater_than_base.append(e)
                else:
                    less_than_base.append(e)

            return __recursively_sort(less_than_base) + equal_base + __recursively_sort(greater_than_base)
        
        result = __recursively_sort(sequence)
        return  result if not reversed else result[::-1]



