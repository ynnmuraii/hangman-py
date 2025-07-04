import random
import os
from pathlib import Path
from hangman_ascii import HANGMAN_PICS, HANGMAN_WELCOME


def get_words_from_file(file_path: str) -> list[str]:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Файл '{file_path}' не найден.")

    with path.open("r", encoding="utf-8") as f:
        words = f.readlines()
    return [word.strip() for word in words if word.strip()]


def get_random_word(words: list[str]) -> str:
    if not words:
        raise ValueError("Список слов пуст. Проверьте файл со словами.")

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
          "\nЕсли ты угадаешь слово, ты выиграл!"
          "\nЕсли ты исчерпаешь попытки, ты проиграл!")

    words = get_words_from_file("words.txt")
    word = get_random_word(words)
    tries = 7
    used_letters = set()
    last_message = ""

    while tries > 0:
        clear_console()

        if last_message:
            print(last_message)
        print(f"\nОсталось попыток: {tries}")
        print("\n", hangman_status(word, used_letters, tries))
        print("\nИспользованные буквы:", " ".join(sorted(used_letters)))
        guess = input("\nВведи букву: ").strip().lower()

        if guess not in alphabet() or len(guess) != 1:
            last_message = ("\nНеверный ввод."
                            "Введи одну букву из русского алфавита.")
            continue

        if guess in used_letters:
            last_message = ("\nЭта буква уже была использована."
                            "Попробуй другую.")
            continue

        if guess in word:
            last_message = "\nПравильно!"
            used_letters.add(guess)
        else:
            last_message = "\nНеверно!"
            used_letters.add(guess)
            tries -= 1

        if all(letter in used_letters for letter in word):
            clear_console()
            print("\nТы выиграл! Твоё слово: ", word)
            return

    clear_console()
    print("\nТы проиграл! Слово было:", word)


def main() -> None:
    while True:
        print(HANGMAN_WELCOME)
        choice: str = input(
            "\nНовая игра? (y/n): ").strip().lower()

        if choice == 'y':
            play_hangman()
        elif choice == 'n':
            print("\nПока пока!")
            break


if __name__ == "__main__":
    main()
