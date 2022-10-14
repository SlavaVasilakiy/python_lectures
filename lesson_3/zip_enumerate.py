users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [1909, 2030, 4056]

data1 = list(enumerate(users))  # enumerate создаёт кортеж из списка, присваивая каждому значению свой индекс
data2 = list(zip(users, ids, salary))  # zip компанует в кортежи значения из списков, работает по минимальному списку
print(data1)
print(data2)