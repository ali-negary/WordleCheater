from suggester.suggest_words import SuggestWords
from suggester.guess_input import UserInput

if __name__ == "__main__":
    # length = input('How many letters in it?')
    length = 5
    print("Enter your guess letter by letter:\n")
    print("(letter (space) state ==> states: (g)reen, (b)lack, (y)ellow.\n")
    # initial values.
    found = False
    i = 0

    # initiate the suggester object.
    suggest = SuggestWords(length)

    # get input, find the word!
    while not found:
        result = False
        letters = UserInput().get_word()
        if letters:
            result = suggest.next_suggestion(letters)
        if result == "continue":
            i += 1
        if result == "out":
            print(
                "We are out of words! You are on your own now, lad or lass or whatever idk."
            )
        if result == "found":
            print("Hooray! You have found the correct word!")
            raise SystemExit
        if i > 4:
            print("You ran out of guesses!")
            raise SystemExit
