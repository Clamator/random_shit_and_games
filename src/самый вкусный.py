class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles


ice1 = IceCream('Chocolate', 13)
ice2 = IceCream('Plain', 18)
ice3 = IceCream('Vanilla', 0)
ice4 = IceCream('Strawberry', 7)
ice5 = IceCream('ChocolateChip', 3)


def sweetest_icecream(lst):
    lst2 = []
    for el in lst:

        dct = {'Chocolate': 10, 'Plain': 0, 'Vanilla': 5, 'Strawberry': 10, 'ChocolateChip': 5}
        if el.flavor in dct.keys():
            lst2.append(dct[el.flavor] + el.sprinkles)
    print(max(lst2))
    return max(lst2)


sweetest_icecream([ice2, ice5])


class IceCream:
    def __init__(self, flavor, sprinkles):
        self.flavor = flavor
        self.sprinkles = sprinkles
