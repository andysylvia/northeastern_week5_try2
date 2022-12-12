t = [[1, 2], [3], [4, 5, 6]]
def nested_sum(t):
    count = 0
    for nestedList in t:
        count += sum(nestedList)
    return count
