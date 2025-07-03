import random
from typing import List
from pathlib import Path

def get_words_from_file(file_path: str) -> List[str]:
    file_path = Path("words.txt")
    with file_path.open("r", encoding="utf-8") as f:
        words = f.readlines()
    return [word.strip() for word in words if word.strip()]

def get_random_word(words: List[str]) -> str:
    return random.choice(words)
 
#def hangman_status(word: str)

def alphabet() -> str:
    return 'абвгдеёжзийклмнопрстуфхчцшщъыьэюя'
 
def play_hangman():
    print("Давай поиграем в \"Виселицу\"!\n У тебя 6 попыток, чтобы угадать слово."
          "\n Если ты угадаешь слово, ты выиграл!\n Если ты исчерпаешь попытки, ты проиграл!\n")
    words = get_words_from_file("words.txt")
    word = get_random_word(words)
    tries = 8
    used_letters = set()
    game_over = False
    print("Загаданное слово:", " _ " * len(word))
    while tries > 0 and game_over == False:
        for tries in range(8, 0, -1):
            print(f"Осталось попыток: {tries}")
            
            guess = input("Введи букву: ").strip().lower()
            if guess not in alphabet():
                print("Неверный ввод. Введи букву из русского алфавита.")
                continue
            if guess in used_letters:
                print("Эта буква уже была использована. Попробуй другую.")
                continue

            if guess in word:
                print("Правильно!")
                used_letters.add(guess)
                
            elif guess not in word:
                print("Неверно!")
                used_letters.add(guess)
                tries -= 1
            
            if tries == 0:
                print("Ты проиграл! Слово было:", word)
                game_over = True
                break
            
            if all(letter in used_letters for letter in word):
                print("Поздравляю! Ты выиграл! Твоё слово: ", word)
                game_over = True
     

while True:
    choice = input("Новая игра? (y/n): ").strip().lower()
    if choice == 'y':
        play_hangman()
    elif choice == 'n':
        print("Пока пока!")
        break

