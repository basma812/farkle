def check_fourkind(dc):
    for i in dc:
        times = dc.count(i)
        if times == 4:
            return 1000
    return 0
