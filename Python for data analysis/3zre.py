f = open('complex.txt','r') # Прочитали файл

f = f.readlines() # Прочитать строки

for i in f:
    print(i,end='\n')
print('Вывод данных файла построчно')

n = int(input('Введите число и на эране появятся числа из файла меньше по модулю этого числа, если нет, увеличьте число: = '))

for i in f:
    i = complex(i) # (complex)
    if abs(i) <= n:
        print(i,'\n')
    else:
        break # Сравнение модулей комплексных чисел из файла с числом и вывод, удовлетворяющих условие

input('Press ENTER to exit')