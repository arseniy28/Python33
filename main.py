from packege.module1 import generate_random_integers, count_doubled_odd_numbers
from packege.module2 import count_word_occurrences

# Задача 1
print("Задача 1: Работа с числами")
file_numbers = "numbers.txt"
generate_random_integers(file_numbers, 100, 1, 100)  
result = count_doubled_odd_numbers(file_numbers)
print(f"Количество удвоенных нечетных чисел: {result}\n")

# Задача 2
print("Задача 2: Работа с текстом")
file_text = "text.txt"
word1 = "слово1"
word2 = "слово2"


word1_count, word2_count, pair_count = count_word_occurrences(file_text, word1, word2)
print(f"Слово '{word1}' встречается {word1_count} раз.")
print(f"Слово '{word2}' встречается {word2_count} раз.")
print(f"Слова '{word1}' и '{word2}' встречаются рядом {pair_count} раз.")
