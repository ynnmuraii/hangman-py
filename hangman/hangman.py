import random
from typing import List
from pathlib import Path

def get_words_from_file(file_path: str) -> List[str]:
    file_path = Path("words.txt")
    with file_path.open("r") as f:
        words = f.readlines()
    return [word.strip() for word in words if word.strip()]

def get_random_word(words: List[str]) -> str:
    return random.choice(words)
 
def hangman_status(word: str)
 



 
def play_hangman():
    print("Let's play Hangman!\n You have 6 tries to guess the word."
          "\n if you guess the word, you win!\n if you run out of tries, you lose!\n")
    words = get_words_from_file("words.txt")
    word = get_random_word(words)
    



    
while True:
    choice = input("New game? (y/n): ").strip().lower()
    if choice == 'y':
        play_hangman()
    elif choice == 'n':
        print("Bye bye, sweetie!")
        break

