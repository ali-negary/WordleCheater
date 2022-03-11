from main.suggest_words import SuggestWords

if __name__ == '__main__':
    # length = input('How many letters in it?')
    # length = 5
    # print("Enter the letters:")
    # word (space) state ==> states: (g)reen, (b)lack, (y)ellow
    found = False
    # while not found:
    #     letters = []
    #     for i in range(1, int(length) + 1):
    #         letter, state = input(f'Letter{i} (space) State').split(' ')
    #         letters.append({'letter': letter.upper(), 'state': state})add
    letters = [{'letter': 'D', 'state': 'y'}, {'letter': 'E', 'state': 'y'},
               {'letter': 'A', 'state': 'y'}, {'letter': 'L', 'state': 'y'},
               {'letter': 'T', 'state': 'b'}]
    guess = ''.join([i['letter'] for i in letters])
    SuggestWords(letters=letters).next_suggestion()
