#%%
from bubble import *
from insertion import *
from selection import *
import random
to_be_sorted = [random.randint(0, 100) for i in range(100)]
%timeit bubble_sort(to_be_sorted)
%timeit bubble_sort_integer(to_be_sorted)
%timeit insertion_sort(to_be_sorted)
%timeit selection_sort(to_be_sorted)
