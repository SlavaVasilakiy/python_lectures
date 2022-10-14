
#def calc1(x):
#    return x*10

# def math(operation, number): # operation - действие(функция) , number - число с котором проводим операцию
    # print(operation(number))

# math(calc1, 20) # вызываем функцию math(просим выполнить операцию calc1, с числом 20)

#--------------------------------------------*---------------------------------------------------------------

# def sum(x, y):
#     return x+y

# s = sum
# sum = lambda x, y: x+y

def mult(x, y):
    return x*y

def calc(operation, a, b):
    print(operation(a, b))
    # return operation(a,b)

calc(lambda x, y: x+y, 4, 5)

