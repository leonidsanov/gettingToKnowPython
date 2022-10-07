# Идея: часто описывать функцию некогда и незачем
# def f(x):
#     return x ** 2


# g = f
# print(f(1))
# print(g(1))
# print(type(f))
# print(type(g))
# print(g(4))
# print(f(5))

# def calc1(x):
#     return x + 10
# # print(calc1(10))
# #
# def calc2(x):
#     return x * 10
# # print(calc2(10))
#
# def math(op, x):
#     print(op(x))
#
# math(calc2, 10)
# math(calc1, 10)

def sum(x, y):
    return x + y

sum = lambda x, y: x + y

def mylt(x, y):
    return x * y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(sum, 2, 4)
calc(lambda c, d: c * d, 5, 6)