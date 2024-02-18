#2. Дана строка в которой слова записаны через пробел. Необходимо перемешать все слова этой строки в случайном порядке.
import random
def shuffle_words(input_string):
    words = input_string.split()
    random.shuffle(words)
    result_string = ' '.join(words)
    return result_string

# Пример использования:
input_string = input("Введите строку слов через пробел: ")
shuffled_string = shuffle_words(input_string)
print(f"Перемешанная строка: {shuffled_string} \n")

#3. Дана строка в которой записаны слова через пробел. Необходимо посчитать количество слов с четным количеством символов.
def count_words(input_string):
    words = input_string.split()
    count_words = sum(len(word) % 2 == 0 for word in words)
    return count_words

# Пример использования:
input_string = input("Введите слова через пробел: ")
result = count_words(input_string)
print(f"Количество слов с четным количеством символов: {result} \n")

#4. Дан массив в котором находятся строки "Белый", "Синий" и "Красный" в случайном порядке. Необходимо упорядочить массив так, чтобы получился российский флаг.
colors = [ "Синий", "Красный","Белый"]
print("Неупорядоченный массив: ", colors)
# Сортировка массива в порядке российского флага
sorted_colors = sorted(colors, key=lambda x: ("Белый", "Синий", "Красный").index(x))

print("Упорядоченный массив для российского флага:", sorted_colors, "\n")
