
def check_sixkind(dc):
    for i in dc:
        times = dc.count(i)
        if times == 6:
            return True 
    return False