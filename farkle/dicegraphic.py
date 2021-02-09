import random

def graphic(list):
    o = "╔═══════╗"
    u = "╚═══════╝"
    one = [o, "║       ║", "║   ■   ║", "║       ║", u]
                        
    two = [o, "║     ■ ║", "║       ║", "║ ■     ║", u]

    three = [o, "║     ■ ║", "║   ■   ║", "║ ■     ║", u]

    four = [o, "║ ■   ■ ║", "║       ║", "║ ■   ■ ║", u]

    five = [o, "║ ■   ■ ║", "║   ■   ║", "║ ■   ■ ║", u]
        
    six = [o, "║ ■   ■ ║", "║ ■   ■ ║", "║ ■   ■ ║", u]

    g = [one, two, three, four, five, six]
    d = len(list)
    printorder = []
    for i in list:
        if i == 1:
            printorder.append(g[0])
        elif i == 2:
            printorder.append(g[1])
        elif i == 3:
            printorder.append(g[2])
        elif i == 4:
            printorder.append(g[3])
        elif i == 5:
            printorder.append(g[4])
        elif i == 6:
            printorder.append(g[5])
        
    for i in range(5):
        for j in range(d):
            if j == d-1:
                print(printorder[j][i])
            else:
                print(printorder[j][i] , end=" ", flush=True)
        



     
    
    