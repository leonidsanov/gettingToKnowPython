# Функции
# Это
# фрагмент
# программы, используемый
# многократно


# def function_name(x):
#   # body line 1
#   # . . .
#   # body line n
#   # optional return

def f(x):
    return x ** 2


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


print(f(1))  # Целое
print(f(2.3))  # 23
print(f(28))  # None
print(type(f(1)))  # str
print(type(f(2.3)))  # int
print(type(f(28)))  # NoneType


def new_string(symbol, count):
    return symbol * count


print(new_string('!', 5))  # !!!!!
print(new_string('!'))  # TypeError missing 1 required ...


def new_string(symbol, count=3):
    return symbol * count


print(new_string('!', 5))  # !!!!!
print(new_string('!'))  # !!!
print(new_string(4))  # 12

# Для ввода неограниченного количества параметров необходимо добавить звездочку
def concatenatio(*params): # неограниченное количество параметров
    res: str = ""

    for item in params:
        res += item
    return res
print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2
# print(conatenatio(1, 2, 3, 4)) # TypeError: ...

# Рекурсия

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)

list = []
for e in range(1, 10):
    list.append(fib(e))
    print(list) # 1 1 2 3 5 8 13 21 34