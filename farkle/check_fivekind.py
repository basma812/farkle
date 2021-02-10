def check_fivekind(dc):
    for i in dc:
        times = dc.count(i)
        if times == 5:
            return True
    return False
