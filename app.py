from main.suggest_words import SuggestWords
from main.guess_input import UserInput

if __name__ == '__main__':
    # length = input('How many letters in it?')
    length = 5
    print("Enter your guess letter by letter:")
    print("(letter (space) state ==> states: (g)reen, (b)lack, (y)ellow.")
    # initial values.
    found = False
    i = 0

    # initiate the suggester object.
    suggest = SuggestWords(length)

    # get input, find the word!
    while not found:
        letters = UserInput().user_input()
        suggest.next_suggestion(letters)
        i += 1
        if i > 4:
            print('You ran out of guesses!')
            raise SystemExit
