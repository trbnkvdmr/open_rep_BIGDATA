import cmath as cm, math as m, time

try:
    N1 = int(input('Введите натуральное число : '))
    N2 = complex(input('Введите комплексное число : '))


    def func(f, N, step=1000000):  # объявили функцию для вычисления времени с локальными переменными
        start_time = time.time()
        for i in range(step):
            f(N)
        Time = time.time() - start_time
        print('%.2f' % Time,
              end='\t')  # добавили end='\t' для переноса на новую строку т.к (строка, добавленная после последнего значения, по умолчанию новая строка)
        return (Time)  # Считали время, исполнили функцию которая возвращает значение переменной Time, вывели её


    def comp(T1, T2):  # бъявили функцию с условиями, для сравнения времени, вывели
        if T1 < T2:
            print('t1 < t2')
        else:
            print('t1 > t2')


    print(' ', 'math', 'cmath', sep='\t   ')

    print('sqrt', end='\t')  # \t\t после вывода названия функции добавили табуляцию

    T1 = func(m.sqrt,
              N1)  # считаем объявленные функции выше, в которых мы выводим значения времени подсчета функций на экран
    T2 = func(cm.sqrt, N2)
    comp(T1, T2)

    print('sin', end='\t\t')  # \t\t для корректного переноса
    T1 = func(m.sin, N1)
    T2 = func(cm.sin, N2)
    comp(T1, T2)

    print('log', end='\t\t')  # \t\t для корректного переноса
    T1 = func(m.log, N1)
    T2 = func(cm.log, N2)
    comp(T1, T2)

except ValueError:
    print('Введите число!!')



