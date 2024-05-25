import random
import string
from words import list_of_words
from hangman_visual import lives_visual_dict


def main():
    try:
        word = word_generator()
        word_letters = set(word)
        used_letters = set()
        word_list = [letter if letter in used_letters else '_' for letter in word]
        alphabet = set(string.ascii_uppercase)
        lives = 7
        while len(word_letters) > 0 and lives > 0:
            word_list = [letter if letter in used_letters else '_' for letter in word]
            print(lives_visual_dict[lives])
            print('Your word ', ''.join(word_list))
            user_letter = input('\nEnter a character: ').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives -= 1
                    print(f'\nThe character {user_letter} is not in the word')
            elif user_letter in used_letters:
                print(f'\nYou have already used {user_letter} try again with a new one')
            else:
                print("\nThis character doesn't exist")
        if lives == 0:
            print(f'\nSorry you lost the word was {word}')
        else:
            print(f'\nCongrats you guessed the word {word}')
        while True:
            play_again_question = input('\nDo you want to play again(yes/no): ').lower()
            if play_again_question == 'yes':
                play_again()
            elif play_again_question == "no":
                quit()
            else:
                print('\nWrong answer')
                continue
    except KeyboardInterrupt:
        print('\nYou left the game')


def word_generator():
    while True:
        word = random.choice(list_of_words)
        if len(word) == 4:
            return word.upper()
        else:
            continue


def play_again():
    main()


if __name__ == '__main__':
    main()
