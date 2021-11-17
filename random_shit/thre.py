import threading
import time


class Counter:
    def __init__(self, lst):
        self.lst = lst
        self.canceled = False
        self.lock_obj = threading.Lock()

    def cancel(self):
        with self.lock_obj:
            self.canceled = True

    def run(self):
        self.counting(self.lst)

    def counting(self, lst):
        for x in set(lst):
            count = lst.count(x)
            print(f'{count} : {x}')
            time.sleep(1.5)
            if self.canceled == True:
                print('Counting was canceled')
                break
            else:
                pass


if __name__ == '__main__':
    print('started main')
    lst = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 4, 5, 1, 2, 3, 1, 4, 5, 7, 6, 8, 7, 8, 6, 5, 6, 7, 8, 6, 5, 4]
    task = Counter(lst)
    t1 = threading.Thread(target=task.run)
    t1.start()  # процесс.старт
    time.sleep(5)
    task.cancel()  # проставляет отмену в тру
    t1.join()
    print('end of main. process was terminated')
