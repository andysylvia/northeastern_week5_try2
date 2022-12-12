t = [1, 2, 3]
def cumsum(t):
    t2 = []
    count = 0
    for i in t:
        count += i
        t2.append(count)
    return t2
