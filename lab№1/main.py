#1. Найти максимальный простой делитель числа
def Prost(num): #Поиск простых чисел.
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def Max_del(number): #Поиск максимального делителя.
    max_del = 1
    for i in range(2, int(number / 2) + 1):
        if number % i == 0 and Prost(i):
            max_del = i
    return max_del

number = int(input("1. Введите число: "))
result = Max_del(number)
print(f"Максимальный простой делитель числа {number}: {result}")
 #2. Найти произведение цифр числа, не делящихся на 5
def res(number):
    product = 1
    for digit in str(number):
        digit = int(digit)
        if digit % 5 != 0:
            product *= digit
    return product

# Пример использования:
number = int(input("2. Введите число: "))
result = res(number)
print(f"Произведение цифр числа {number}, которые не делятся на 5: {result}")
 #3. Найти НОД максимального нечетного непростого делителя
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
def max_odd_composite_divisor(number):
    max_divisor = 1
    for i in range(3, int(number / 2) + 1, 2):
        if number % i == 0 and not is_prime(i):
            max_divisor = i
    return max_divisor

# Пример использования:
number = int(input("3. Введите число: "))
max_odd_composite = max_odd_composite_divisor(number)
result = gcd(number, max_odd_composite)
print(f"НОД максимального нечетного непростого делителя {max_odd_composite} и числа {number}: {result}")
