#Подсчет кол-во упомянутых слов
def count_word_occurrences(file_name, word1, word2):
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
    count_word1 = text.count(word1)
    count_word2 = text.count(word2)
    count_pair = text.count(f"{word1} {word2}") + text.count(f"{word2} {word1}")
    return count_word1, count_word2, count_pair
