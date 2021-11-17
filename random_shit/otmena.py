import multiprocessing
import time


def counting(lst):
    for x in set(lst):
        count = lst.count(x)
        print(f'{count} : {x}')
        time.sleep(1.5)


if __name__ == '__main__':
    print('start')
    lst = [1, 2, 4, 1, 2, 4, 5, 6, 4, 3, 2, 4, 3, 4, 5, 4, 3, 2, 1, 4, 3, 5, 6, 5, 4, 1, 2, 1, 2, 2]

    p1 = multiprocessing.Process(target=counting, args=(lst,))
    p1.start()
    time.sleep(5)
    p1.terminate()
    print('process was terminated')