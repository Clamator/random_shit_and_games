def avg(a, b, c):
    return (a + b + c) / 3


print(avg(1, 2, 3))
print(avg(c=3, a=1, b=2, ))
# для того, чтобы делать аргументы позиционными, то есть в соответствии с тем, как они указаны в ф-и изначально,
# без смешивания как во втором выводе, надо поставить / после указания аргументов
def avg2(a, b, c, /):
    return (a + b + c) / 3


print(avg2(1, 2, 3))


# print(avg2(c= 1, b =2, a =3))

# можно перемежать позиционные и keyword аргументы

def assert_equal(left, right, /, fail_message='pass'):
    return (left == right, fail_message)


print(assert_equal(1, 1))
print(assert_equal(1, 1, fail_message='typing text...'))


# бывает, надо явно указать keyword аргумменты, то есть с указанием имени именно
# для этого ставится * перед называемыми аргументами

def summa(*, a, b, c):
    return a + b + c


# если тут не указать имена переменных, ничего не выйдет
print(summa(a=1, b=2, c=3))


# эти темы можно сочетать

def summa2(a, b, /, *, c):
    return a + b + c


print(summa2(2, 4, c=3))

# название аргументы принудительно через * имеет смысл навязывать при передачи булиевых значений, например
# или для того, чтобы смысл какого-то аргумента не пропал