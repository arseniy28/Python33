#Генерация случ. числ в файл и подсчет удвоинеых нечет. чисел
import random
def generate_random_integers(file_name, count, range_min, range_max):
    with open(file_name, "w") as f:
        for _ in range(count):
            f.write(f"{random.randint(range_min, range_max)}\n")
def count_doubled_odd_numbers(file_name):
    count = 0
    with open(file_name, "r") as f:
        for line in f:
            number = int(line.strip())
            if number % 2 != 0 and (number * 2) % 2 == 0:
                count += 1
    return count
