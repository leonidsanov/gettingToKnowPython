# для быстрого создания списков
list = []

for i in range(1, 10):
    if(i % 2 == 0):
        list.append(i)

print(list)

list = [i for i in range(1, 10)]
print(list)

list = [i for i in range(1, 10) if i % 2 == 0]
print(list)

# Список кортежей
list = [(i, i) for i in range(1, 10) if i % 2 == 0]
print(list)

def f(x):
    return x**3

list = [f(i) for i in range(1, 10) if i % 2 == 0]
print(list)

list = [(i, f(i)) for i in range(1, 10) if i % 2 == 0]
print(list)

list = [1, 2, 3, 5, 8, 15, 23, 38]
for i in range(len(list)):
    if(i % 2 == 0):
        i**2
        print((i, i**2))