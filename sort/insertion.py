# %%
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

def swap(a_list, i, j):
    a_list[i], a_list[j] = a_list[j], a_list[i]



# %%
