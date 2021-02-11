# checks four of a kind plus a pair
def check_fourpluspair(dc):
    for i in dc:
        # times is how many times the element occurs in the list
        times = dc.count(i)
        if times == 4:
            k = i
            for j in dc:
                if k != j:
                    times = dc.count(j)
                    if times == 2:
                        return 1500
    return 0
