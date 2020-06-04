import array as arr
def bubble_sort(a_list):
    sorted_list = []
    to_sort = a_list
    for i in range(len(a_list)):
        to_sort = one_pass(to_sort)
        left_most = to_sort[0]
        sorted_list.append(left_most)
        to_sort = to_sort[1:]
    return  sorted_list

def one_pass(a_list):
    for i in range(len(a_list) - 1):
        if a_list[-(i+1)] < a_list[-(i+2)]:
            tmp = a_list[-(i+2)]
            a_list[-(i+2)] = a_list[-(i+1)]
            a_list[-(i+1)] = tmp

    return a_list

def one_pass_verbose(a_list):
    for i in range(len(a_list) - 1):
        if a_list[-(i+1)] < a_list[-(i+2)]:
            print("at indexes", -(i+2), -(i+1) )
            tmp = a_list[-(i+2)]
            a_list[-(i+2)] = a_list[-(i+1)]
            a_list[-(i+1)] = tmp
            print("swapping", a_list[-(i+1)],a_list[-(i+2)], "to", 
                a_list[-(i+2)],a_list[-(i+1)])
    
    print("array after bubble up", a_list)
    return a_list

def bubble_sort_integer(a_list):
    for i in range(len(a_list)):
        a_list[i:] = one_pass(a_list[i:])
    return  a_list

def bubble_sort_verbose(a_list):
    a_array = list_to_array(a_list)
    print("array to sort", a_array)
    for i in range(len(a_array)):
        a_array[i:] = one_pass_verbose(a_array[i:])
    return  a_array

def list_to_array(a_list):
    return arr.array("i", a_list)