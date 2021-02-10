def check_sixkind(dc):
    for i in dc:
        times = dc.count(i)
        if times == 6:
            if i == 1:
                return 10000
            return 3000
    return 0


