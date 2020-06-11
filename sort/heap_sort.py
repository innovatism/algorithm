# %%
from .common.utils import swap



def build_heap_struct(n):
    heap_record = {}
    reversed_heap_record = {}
    for i in range(n):
        idx = 2*i + 1
        if idx < n - 1:
            heap_record[i] = [idx, idx + 1]
        elif idx == n - 1:
            heap_record[i] = [idx]
        else:
            heap_record[i] = []
    for i in heap_record:
        for j in heap_record[i]:
            reversed_heap_record[j] = i

    return heap_record, reversed_heap_record


def one_pass(a_list, hs):
    changed = False
    for i in range(len(a_list)):
        for j in hs[i]:
            if a_list[j] > a_list[i]:
                #print(f"swapping a[{i}]={a_list[i]}, a[{j}]={a_list[j]}")
                swap(a_list, i, j)
                changed = True
    return changed


def one_pass_v2(a_list, r_hs):
    changed = False
    for i, j in r_hs.items():
        if a_list[j] < a_list[i]:
            #print(f"swapping a[{i}]={a_list[i]}, a[{j}]={a_list[j]}")
            swap(a_list, i, j)
            changed = True
    return changed


def put_list_in_heap(a_list):
    hs, r_hs = build_heap_struct(len(a_list))
    i = 0
    while True:
        i += 1
        if not one_pass(a_list, hs):
            break

    return a_list


# %%
_input = [5, 2, 7, 3, 6, 1, 4, 9, 10, 20, 0, 8]
_output = [8, 7, 6, 5, 2, 3, 1, 4]
ans = put_list_in_heap(_input)


def heap_sort(a_list):
    a_list = put_list_in_heap(a_list)
    length = len(a_list)
    sorted = []
    for i in range(length):
        swap(a_list, 0,  -1)
        sorted.insert(0, a_list.pop())
        a_list = put_list_in_heap(a_list)

    return sorted
# %%
heap_sort(_input)

# %%
