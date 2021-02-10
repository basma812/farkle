#checks if its a straight from 1-6
def check_straight(l):
    l.sort()
    if len(l) != 6:
        return False
    if l[0] != l[1]:
        if l[1] != l[2]:
            if l[2] != l[3]:
                if l[3] != l[4]:
                    if l[4] != l[5]:
                        return 1500
                    
    return 0