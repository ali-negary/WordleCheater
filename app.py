from main.suggest_words import SuggestWords

if __name__ == '__main__':
    # length = input('How many letters in it?')
    length = 5
    # print("Enter the letters:")
    # word (space) state ==> states: (g)reen, (b)lack, (y)ellow
    found = False
    letterssss = [
        [{'letter': 'D', 'state': 'y'}, {'letter': 'E', 'state': 'y'},
         {'letter': 'A', 'state': 'y'}, {'letter': 'L', 'state': 'y'},
         {'letter': 'T', 'state': 'b'}],
        [{'letter': '', 'state': ''}, {'letter': '', 'state': ''},
         {'letter': '', 'state': ''}, {'letter': '', 'state': ''},
         {'letter': '', 'state': ''}]
    ]
    i = 0
    while not found:
        # letters = []
        # for i in range(1, int(length) + 1):
        #     letter, state = input(f'Letter{i} (space) State').split(' ')
        #     letters.append({'letter': letter.upper(), 'state': state})
        letters = letterssss[i]
        guess = ''.join([i['letter'] for i in letters])
        next_sug = SuggestWords(letters=letters, length=length).next_suggestion()
        print(next_sug)
        i += 1
