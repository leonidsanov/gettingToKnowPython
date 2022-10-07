# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми
# объектами.
# f(x) ⇒ x + 10
# map(f, [1, 2, 3, 4, 5])
# ↓ ↓ ↓ ↓ ↓
# [11, 12, 13, 14, 15]
# Нельзя пройтись дважды
# 34-я минута видео, 13 страница презентации

li = [x for x in range(1, 20)]

li = map(lambda x: x + 10, li)

lis = list(map(lambda x: x + 10, li))

print(li)
print(lis)

#################

data = list(map(int, input().split()))
print(data)

data = list(map(int, '1 2 3'.split()))

for e in data:
    print(e)

print('--')

for e in data:
    print(e)