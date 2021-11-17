import time


def printer(lst, thread_name='t'):
    print(f'smth happens in {thread_name}')
    for x in lst:
        if x % 3 != 0 and x % 7 != 0:
            print(f'{x} - unknown statement')
            time.sleep(0.5)
        if x % 3 == 0:
            print(f'{x} = threesome')
            time.sleep(0.5)
        if x % 7 == 0:
            print(f'{x} = five corners')
            time.sleep(0.5)
    print('all done')
