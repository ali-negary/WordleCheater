class UserInput:
    def __init__(self):
        pass

    @staticmethod
    def user_input():
        word = input("Enter your guess: ")
        states = input("Enter corresponding status of your guess: ")

        if all([st == "g" for st in states]):
            states = "ggggg"
        elif all([st == "b" for st in states]):
            states = "bbbbb"
        elif all([st == "y" for st in states]):
            states = "yyyyy"

        letters = [{'letter': word[index].upper(), 'state': states[index]}
                   for index in range(len(word))]

        print(f"Current guess: {word.capitalize()} : {states}")
        return letters
