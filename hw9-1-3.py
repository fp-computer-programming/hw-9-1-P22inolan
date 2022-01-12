# Author: IBN (AMDG) 1/12/2022

def find_thing(lst, x):
    try:
        for i, v in enumerate(lst):
            if v == x:
                find = i
                return i
                break
    finally:
        try:
            if find == i:
                return find
        except UnboundLocalError:
            return "-1"

print(find_thing(["orange", "banana"], "banana"))