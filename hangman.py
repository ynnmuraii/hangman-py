import random
import os
from typing import List
from pathlib import Path
from hangman_ascii import HANGMAN_PICS, HANGMAN_WELCOME


def get_words_from_file(file_path: str) -> List[str]:
    file_path = "words.txt"
    with open(file_path, "r", encoding="utf-8") as f:
        words = f.readlines()
    return [word.strip() for word in words if word.strip()]


def get_random_word(words: List[str]) -> str:
    return random.choice(words)


def hangman_status(word: str, used_letters: set[str], tries: int) -> str:
    status_letters = []
    for letter in word:
        if letter in used_letters:
            status_letters.append(letter)
        else:
            status_letters.append("_")
    print(HANGMAN_PICS[7 - tries])
    return " ".join(status_letters)


def alphabet() -> str:
    return 'абвгдеёжзийклмнопрстуфхчцшщъыьэюя'


def clear_console() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def play_hangman() -> None:
    clear_console()
    print("\nУ тебя 7 попыток, чтобы угадать слово."
          "\nЕсли ты угадаешь слово, ты выиграл!\nЕсли ты исчерпаешь попытки, ты проиграл!")
    words = get_words_from_file("words.txt")
    word = get_random_word(words)
    tries = 7
    used_letters = set()

    while tries > 0:
        print(f"\nОсталось попыток: {tries}")
        print("\n", hangman_status(word, used_letters, tries))
        print("\nИспользованные буквы:", " ".join(sorted(used_letters)))
        guess = input("\nВведи букву: ").strip().lower()
        if guess not in alphabet() or len(guess) != 1:
            clear_console()
            print("\nНеверный ввод. Введи одну букву из русского алфавита.")
            continue

        if guess in used_letters:
            clear_console()
            print("\nЭта буква уже была использована. Попробуй другую.")
            continue

        if guess in word:
            clear_console()
            print("\nПравильно!")
            used_letters.add(guess)

        elif guess not in word:
            clear_console()
            print("Неверно!")
            used_letters.add(guess)
            tries -= 1

        if tries == 0:
            clear_console()
            print("\nТы проиграл! Слово было:", word)

        if all(letter in used_letters for letter in word):
            clear_console()
            print("\nТы выиграл! Твоё слово: ", word)
            break


while True:
    print(HANGMAN_WELCOME)
    choice: str = input(
        "\nНовая игра? (y/n): ").strip().lower()
    if choice == 'y':
        play_hangman()
    elif choice == 'n':
        clear_console()
        print("\nПока пока!")
        break
