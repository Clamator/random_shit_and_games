

def count_vowels(string):
    lst = ['a', 'e', 'i', 'o', 'u']
    num = 0
    for el in string:
        if el in lst:
            num += 1
    print(num)

count_vowels('aaaaaa')


