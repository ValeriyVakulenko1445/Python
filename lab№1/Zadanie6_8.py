#3. Дана строка. Необходимо найти общее количество русских символов.
def Count_Russian_Simbols(input_string):
    # Определение функции count_russian_characters с одним параметром input_string.
    russian_characters = []
    for symbol in input_string:
        unicode_value = ord(symbol)
        # Получение числового значения Unicode для текущего символа и сохранение его в переменной unicode_value.
        if 1040 <= unicode_value <= 1103:
            # Проверка, находится ли символ в диапазоне русских букв в Unicode.
            russian_characters.append(symbol)
            # Если символ русский, то он добавляется в список russian_characters.
    count = len(russian_characters)
    # Подсчет количества русских символов в списке russian_characters.
    return count
input_string = input("Введите строку: ")
result = Count_Russian_Simbols(input_string)
print(f"Общее количество русских символов: {result}")

#8. Дана строка. Необходимо найти все используемые в ней строчные символы латиницы.
def Latin_Simbols(input_string):
    latin_chars =[symbol for symbol in input_string if 'a' <= symbol <= 'z' ]
    uniq_simb = set(latin_chars)
    count = len(uniq_simb)
    print(count)
    return uniq_simb
input_string = input("Введите строку символов через пробел :")
result = Latin_Simbols(input_string)
print(f"Используемые символы латиницы :{result}")

