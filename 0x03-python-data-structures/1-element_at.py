#!/usr/bin/python3
def element_at(my_list, ids):
    if ids < 0:
        return None
    elif ids >= len(my_list):
        return None
    else:
        return (my_list[ids])
