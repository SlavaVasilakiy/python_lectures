def select(f, col):             # res = select(int, data)
                                # res = select(lambda x: (x, x ** 2), res)
    return [f(x) for x in col]  # в f записывается задача для каждого числа в списке data присваивается целочисленное значение int
                                # в f записывается выражение lambda x: (x, x ** 2), в списке res

def where(f, col):                      # res = where(lambda x: not x % 2, res)
    return [x for x in col if f(x)]     # в f записывается выражение lambda x: not x % 2, в списке res

data = '1 2 3 5 8 15 23 38'.split()  # split по умолчанию в скобках имеет значение пробела

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)

print(res)