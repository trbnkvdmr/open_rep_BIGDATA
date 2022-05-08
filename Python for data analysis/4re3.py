def zad4(*nums):

    if len(nums) == 0:
        return (60)

    elif len(nums) == 1:
        return ('Ошибка')

    elif len(nums) == 2:
        s = 0
        for i in nums:
            s+=i
        return (s)

    elif len(nums) == 3:
        s = 1
        for i in nums:
            s*=i
        return (s)

    else:
        print('Ошибка')
    exit()

print(zad4())

print(zad4(1.0))

print(zad4(1.0, 5.0))

print(zad4(2.0, 5, 7))

print(zad4(1.0, 2.0, 5, 7))
