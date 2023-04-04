def hello():
    print('Hello World!')


def chf(a):
    if a % 2 == 0:
        a += 2
        print(a)
    elif a % 2 == 1:
        a += 1
        print(a)


def ch(a):
    if a % 2 == 0:
        print(1)
    else:
        print(0)


def issym(a):
    reva = a[::-1]
    if reva == a:
        print(True)
    else:
        print(False)


def summ(a):
    summa = 0
    for i in a:
        summa += int(i)
    print(summa)


def prossl(a):
    if a <= 1:
        return False
    for i in range(2, int(a**0.5)+1):
        if a % i == 0:
            return False
    return True


while True:
    print('Выберите команду')
    print('1. Hello World!')
    print('2. Ближайшее чётное число')
    print('3. Проверка чётности')
    print('4. Проверка симметрии числа')
    print('5. Сумма чисел')
    print('6. Сумма чисел')
    print('7. Сумма чисел')
    print('8. Проверка на простое или сложное число')

    choice = int(input())
    if choice == 1:
        hello()
    elif choice == 2:
        print('Введите число')
        a = int(input())
        chf(a)
    elif choice == 3:
        print('Введите число')
        b = int(input())
        chf(b)
    elif choice == 4:
        с = input()
        issym(с)
    elif choice == 5:
        d = input()
        summ(d)
    elif choice == 6:
        e = input()
        summ(e)
    elif choice == 7:
        f = input()
        summ(f)
    elif choice == 8:
        g = int(input())
        print(prossl(g))
    else:
        print('')
