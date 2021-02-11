#vi ska checka ettor och femmor. ettor ger 100 styck och femmor 50.
#först måste vi kolla så att det inte är ettor eller femmor i triss, fyrtal, eller femtal
#t ex om det är ettor i triss och vi har två femmor. då ska vi inte checka efter ettor
#eftersom de redan är i trissen

def checkones(dr):
    for i in dr:
        if i == 1:
            times = dr.count(i)
            if times == 1:
                return 100
            if times == 2:
                return 200
    return 0             
def checkfives(dr):
    for i in dr:
        if i == 5:
            times = dr.count(i)
            if times == 1:
                return 50
            if times == 2:
                return 100  
    return 0
def check_one_and_fives(dr):
    sum = 0
    for i in dr:
        times = dr.count(i)
        if times == 5:
            if i == 5:
                return checkones(dr)
            if i == 1:
                return checkfives(dr)
        if times == 4:
            if i == 5:
                return checkones(dr)
            if i == 1:
                return checkfives(dr)
        if times == 3:
            if i == 5:
                return checkones(dr)
            if i == 1:
                return checkfives(dr)
        else:
            if i == 1:
                times = dr.count(i)
                if times == 1:
                    sum+= 100
                if times == 2:
                    sum+= 200
            if i == 5:
                times = dr.count(i)
                if times == 1:
                    sum+= 50
                if times == 2:
                    sum+= 100
    return sum  

        
