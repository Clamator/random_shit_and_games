import threading
import time


class Svetofor:
    def __init__(self):
        self.svetofor = threading.Event()

    def stop(self):
        self.svetofor.clear()

    def go(self):
        self.svetofor.set()

    def main(self):
        print('green light')
        counter = 0
        counter_total = 0
        self.go()
        self.svetofor.wait()
        for x in range(1, 20):
            print(x)
            time.sleep(0.5)
            counter += 1
            counter_total += 1
            if counter == 10:
                self.stop()
                break

        print('RED light')
        time.sleep(5)
        print('yellow light, prepare to start')
        time.sleep(2)

        if counter_total <= 2:
            self.main()
        else:
            print('svetofor is broken')

if __name__ == '__main__':
    sv = Svetofor()
    sv.main()
