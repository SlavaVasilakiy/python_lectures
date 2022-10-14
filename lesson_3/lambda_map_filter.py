data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)                         # map - используется для цикличности функции описанной внутри скобок
                                             # было вот так: res = select(int, data) -> def select(f, col): return [f(x) for x in col]

res = list(filter(lambda x: not x % 2, res))  # filter - осуществляет выборку по условию lambda
                                              # было: res = where(lambda x: not x % 2, res) -> def where(f, col): return [x for x in col if f(x)]

res = list(map(lambda x: (x, x ** 2), res))  # list создаёт список на основе цикличной функции map с выражением lambda

print(res)