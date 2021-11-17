class Wallet:
    file = 'smth.txt'

    def __init__(self):
        self.balance = 0
        self.amount = 0

    def refill(self):
        file = 'smth.txt'
        refil = input('how much to refill?: ')
        with open(file, 'r') as f:
            total_money = f.read()
            print(f'operation of refilling is in progress. {total_money} was in wallet')
            new_money = float(total_money) + float(refil)
            print(f'now it is {new_money} in wallet')
        with open(file, 'w') as f:
            new_money = str(new_money)
            f.write(new_money)

    def withdraw(self):
        file = 'smth.txt'
        w_d = input('how much to withdraw?: ')
        with open(file, 'r') as f:
            total_money = f.read()
            print(f'operation of withdrawing is in progress. {total_money} was in wallet')
            new_money = float(total_money) - float(w_d)
            print(f'now it is {new_money} in wallet')
        with open(file, 'w') as f:
            new_money = str(new_money)
            f.write(new_money)

    def __str__(self):
        return f'total amount of money is {self.balance}'


if __name__ == '__main__':
    wallet = Wallet()
    wallet.refill()
