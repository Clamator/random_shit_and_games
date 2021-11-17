print(walrus := True)

for i in range(rows := int(input('enter a number of rows: '))):
    print('*' * (i + 1))


# тут сразу запихнули переменную в range, и имя присвоили, и сократили количество строк

# кроме того, можно пихать walrus почти куда угодно

def read_file(text):
    while True:
        line = text.readline()
        if not line:
            break

        split_line = line.split(';')
        print(split_line[0])


def read_file2(text):
    while line := text.readline():
        if not line:
            break

        split_line = line.split(';')
        print(split_line[0])