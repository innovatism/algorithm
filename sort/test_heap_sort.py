from .heap_sort import *

def test_put_list_in_heap():
    _input = [5 ,2 , 7, 3, 6, 1, 4]
    _output = [7, 6, 5, 2, 3, 1, 4]
    assert put_list_in_heap(_input) == _output

def test_heap_sort():
    _input = [5 ,2 , 7, 3, 6, 1, 4]
    _output = [1, 2, 3, 4, 5, 6, 7]
    assert heap_sort(_input) == _output