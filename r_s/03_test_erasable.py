file = 'smth.txt'


def refill():
    refil = input('how much to refill?: ')
    with open(file, 'r') as f:
        total_money = f.read()
        print(f'operation of refilling is in progress. {total_money} was in wallet')
        new_money = float(total_money) + float(refil)
        print(f'now it is {new_money} in wallet')
    with open(file, 'w') as f:
        new_money = str(new_money)
        f.write(new_money)


def withdraw():
    w_d = input('how much to withdraw?: ')
    with open(file, 'r') as f:
        total_money = f.read()
        print(f'operation of withdrawing is in progress. {total_money} was in wallet')
        new_money = float(total_money) - float(w_d)
        print(f'now it is {new_money} in wallet')
    with open(file, 'w') as f:
        new_money = str(new_money)
        f.write(new_money)


if __name__ == '__main__':

    x = input('what do you want? refill(1) or withdraw(0)')
    if x == 1 or x == "1":
        refill()
    elif x == 0 or x == '0':
        withdraw()
    else:
        raise Exception('Unknown operation')
