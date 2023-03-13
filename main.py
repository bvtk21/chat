import random
import requests

# Загрузить список слов из текстового файла по ссылке
response = requests.get("https://raw.githubusercontent.com/bvtk21/chat/main/worlds.txt")
word_list = response.text.strip().split('\n')

# Выбрать случайное слово
current_word = random.choice(word_list)

# Основной цикл программы
while True:
    print("Текущее слово: " + current_word)
    command = input("Введите команду (1 - выбрать новое слово, любой другой символ - продолжить): ")
    
    if command == "1":
        current_word = random.choice(word_list)
    else:
        continue
