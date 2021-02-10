#checkar om det är trepar, returnerar True eller False
def check_three_pairs(list):
    list.sort()
    if len(list) != 6:
        return False
    elif list[0] == list[1]:
        if list[2] == list[3]:
            if list[4] == list[5]:
                if list[0] != list[2]:
                    if list[2] != list[4]:
                        return True
    return False