# %%
from .bubble import *
import pytest


def test_bubble():
    _input = [5, 4, 6, 0, 1, 2]
    _output = [0, 1, 2, 4, 5, 6]
    assert bubble_sort(_input) == _output

def test_bubble_integer():
    _input = [5, 4, 6, 0, 1, 2]
    _output = [0, 1, 2, 4, 5, 6]
    assert bubble_sort_integer(_input) == _output
# %%
