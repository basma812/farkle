import random
diceroll = [random.randrange(1, 6, 1) for i in range(6)]
# def graphic():
o = "╔═══════╗"
u = "╚═══════╝"
one = [o, "║       ║", "║   ■   ║", "║       ║", u]
                    
two = [o, "║     ■ ║", "║       ║", "║ ■     ║", u]

three = [o, "║     ■ ║", "║   ■   ║", "║ ■     ║", u]

four = [o, "║ ■   ■ ║", "║       ║", "║ ■   ■ ║", u]

five = [o, "║ ■   ■ ║", "║   ■   ║", "║ ■   ■ ║", u]
    
six = [o, "║ ■   ■ ║", "║ ■   ■ ║", "║ ■   ■ ║", u]

g = [one, two, three, four, five, six]
d = len(diceroll)
printorder = []
for i in diceroll:
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
            print(printorder[j][i] , end="\n", flush=True)
        else:
            print(printorder[j][i] , end=" ", flush=True)
        



     
    
    