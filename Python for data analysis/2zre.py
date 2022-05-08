q=[]
# Создание пустого списка
q0=int(input('Введите 1 элемент списка(int): '))
q.insert(0, q0)
q1=float(input('Введите 2 элемент списка(float): '))
q.insert(1, q1)
q2=complex(input('Введите 3 элемент списка(complex): '))
q.insert(2, q2)
# Запрашиваем элементы списка

try:
    q0 = float(q0)
except ValueError:
    q0 = str(q0)

try:
    q1 = int(q1)
except ValueError:
    q1 = str(q1)

try:
    q2 = int(q2)
except TypeError:
    q2 = str(q2)
try:
    q2 = float(q2)
except ValueError:
    q2 = str(q2)

# try перевода каждого в тип, если нет то перевод в строку

print(q)

keys = (type(q0), type(q1), type(q2))

T = dict(zip(keys, q)) # словарь с ключами(типы переменных в словаре) и значениями

print(T)

T = str(T)
file = open('2z.txt','w')
file.write(T)
file.close()

# Запись словаря в файл в формате строки

input('Press ENTER to exit')
