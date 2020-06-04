from .selection import selection_sort
import pytest

def test_selection_sort():
    _input = [5, 4, 6, 0, 1, 2]
    _output = [0, 1, 2, 4, 5, 6]
    assert selection_sort(_input) == _output 