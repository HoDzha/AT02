def count_vowels(word):
    vowels = set("аеёиоуыэюяaeiou")  # Используем set для быстрого поиска
    count = 0
    for char in word.lower():
        if char in vowels:
            count += 1
    return count

# # Пример использования
# word = input("Введите слово: ")
# print(f"Количество гласных в слове '{word}': {count_vowels(word)}")


