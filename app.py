from main.suggest_words import SuggestWords

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
        word = input("Enter your guess: ")
        status = input("Enter corresponding status of your guess: ")
        letters = [{'letter': word[index].upper(), 'state': status[index]}
                   for index in range(len(word))]
        # for index in range(1, int(length) + 1):
        #     letter, state = input(f'Letter{index} State\n').split(' ')
        #     letters.append({'letter': letter.upper(), 'state': state})
        print(f"current guess: {word.upper()}")
        suggest.next_suggestion(letters)
        i += 1
        if i > 4:
            print('You ran out of guesses!')
            raise SystemExit
