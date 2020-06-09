
from collections import Iterable
from functools import reduce
import more_itertools
from operator import add


class ListHandler:

    @staticmethod
    def handler_1(items):
        for element in items:
            if isinstance(element, Iterable) and not isinstance(element, (str, bytes)):
                for sub_element in ListHandler.handler_1(element):
                    yield sub_element
            else:
                yield element

    @staticmethod
    def handler_2(items):
        empty_lst = []
        for element in items:
            if isinstance(element, int):
                empty_lst.append(element)
            else:
                empty_lst.extend(ListHandler.handler_2(element))
        return empty_lst

    @staticmethod
    def handler_3(items, lst=None):
        if lst is None:
            lst = []
        for element in items:
            if isinstance(element, list):
                ListHandler.handler_3(element, lst)
            else:
                lst.append(element)
        return lst

    @staticmethod
    def handler_4(lst):  # только для int
        flatten = lambda lst: [lst] if isinstance(lst, int) else reduce(
            add, [flatten(ele) for ele in lst]
        )
        return flatten(lst)

    @staticmethod
    def handler_5(items):
        result = list(more_itertools.collapse(items))
        return result


if __name__ == '__main__':
    lst = [1, [2, [3, 4], 5], [[6, [7, [8, 9]]]]]
    str_lst = ['Dave', 'Paula', ['Thomas', ['Lewis', "Andre"]]]

    extended_lst = list(ListHandler.handler_4(str_lst))
    print(extended_lst)
