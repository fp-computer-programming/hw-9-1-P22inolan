# Author: IBN (AMDG) 1/12/2022

def even_index(lst):
    new_lst = []
    for i, v in enumerate(lst):
        if i % 2 == 0:
            new_lst.append(v)
    return new_lst

print(even_index([1, 3, 4, 6, 8, 2, 0]))