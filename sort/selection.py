# %%
import operator
def selection_sort(a_list):
    for i in range(len(a_list)):
        index_min, val_min = min(enumerate(a_list[i:]), key=operator.itemgetter(1))
        a_list[index_min + i], a_list[i] = a_list[i], a_list[index_min + i]
    return a_list



# %%
