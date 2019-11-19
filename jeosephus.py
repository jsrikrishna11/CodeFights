soldiers = 7

circle = list(range(soldiers))
"""
Kill variable indicates which soldier is going to die next


"""

def jeosephus(circle):
    kill = 1
    while circle.__len__() > 1:
        length = circle.__len__()
        if kill > length:
            i = kill % length
        circle[kill] = -1
        kill = kill + 1
    return circle[0]

print(jeosephus(circle))