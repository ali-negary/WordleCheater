class UserInput:
    def __init__(self):
        self.word = []

    def user_input(
        self,
    ):
        word = input("Enter your guess: \n")
        states = input("Enter corresponding status of your guess: \n")

        if all([st == "g" for st in states]):
            states = "ggggg"
        elif all([st == "b" for st in states]):
            states = "bbbbb"
        elif all([st == "y" for st in states]):
            states = "yyyyy"

        letters = [
            {"letter": word[index].upper(), "state": states[index]}
            for index in range(len(word))
        ]

        print(f"Current guess: {word.capitalize()} : {states}")
        self.word = letters

    def validate_input(
        self,
    ):
        if len(self.word) != 5:
            print("Invalid input. Please enter 5 letters")
            return False
        for letter in self.word:
            if letter["state"] not in ["g", "b", "y"]:
                print("Invalid input. Please enter g, b or y")
                return False
        return True

    def get_words(
        self,
    ):
        self.user_input()
        valid = self.validate_input()
        if valid:
            return self.word
        else:
            return False
