from .insertion import insertion_sort

def test_insertion_sort():
    _input = [5, 4, 6, 0, 1, 2]
    _output = [0, 1, 2, 4, 5, 6]
    
    assert insertion_sort(_input) == _output