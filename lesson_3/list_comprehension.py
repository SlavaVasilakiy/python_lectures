# list = []
#
# for i in range (1, 101):
#     if(i % 2 == 0):
#         list.append(i)
def f(x):
    return x**3

lst1 = [f(i) for i in range(1, 11) if i % 2 == 0] # список

lst2 = [(i, f(i)) for i in range(1, 11) if i % 2 == 0] # кортеж

print(lst1)
print(lst2)
