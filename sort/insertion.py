# %%
from .common.utils import swap
def insertion_sort(a_list):
    for i in range(len(a_list) - 1):
        cursor = i + 1
        for j in reversed(range(i + 1)):
            if a_list[cursor] < a_list[j]:
                swap(a_list, cursor, j)
                cursor = j
            else:
                break
            
            if j == 0:
                break
            
    return a_list




# %%
