# checks if its a straight from 1-6
def check_straight(lst):
    lst.sort()
    if len(lst) != 6:
        return False
    if lst[0] != lst[1]:
        if lst[1] != lst[2]:
            if lst[2] != lst[3]:
                if lst[3] != lst[4]:
                    if lst[4] != lst[5]:
                        return True

    return False
