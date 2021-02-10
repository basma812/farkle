def check_fivekind(dc):
    for i in dc:
        times = dc.count(i)
        if times == 5:
            return 2000
    return 0
