


def check_sequence(lst):
    lst2 = []
    for x in range(0, len(lst) - 1):
        if lst[x] < lst[x + 1]:
            lst2.append(1)
        elif lst[x] > lst[x + 1]:
            lst2.append(-1)
        else:
            pass

        if lst2.count(1) == len(lst2):
            return 1
        elif lst2.count(-1) == len(lst2):
            return -1
        else:
            return 0


check_sequence([1, 2, 0])
