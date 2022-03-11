import requests


class SuggestWords:
    """This class gets the info on the words.
    Then, suggest a list of words based on the info."""

    def __init__(self, letters: list) -> None:
        self.base_url = 'https://wordfinderx.com/words-for/_/'
        self.letters = letters
        self.start = ''
        self.end = ''
        self.substring = ''
        self.length = ''
        self.include = ''
        self.exclude = ''
        self.url = ''
        self.words = []

    def process_letters_for_url(self, ) -> None:
        """Processes the letters to create the url"""
        # find exclude and include
        for item in self.letters:
            if item['state'] == 'b':
                self.exclude += item['letter']
            else:
                self.include += item['letter']
        # find start and end and initiate substring
        if self.letters[0]['state'] == 'g':
            self.start = self.letters[0]['letter']

        if self.letters[-1]['state'] == 'g':
            self.end = self.letters[-1]['letter']
        # find substring
        for index in range(1, len(self.letters)):
            current = self.letters[index]
            previous = self.letters[index - 1]
            if current['state'] == 'g' and previous['state'] != 'g':
                self.substring = current['letter']
            if current['state'] == 'g' and previous['state'] == 'g':
                self.substring += current['letter']
            else:
                self.substring = ''

    def create_url(self, ) -> None:
        """Creates an url to wordfinderx.com"""
        start_with = '' if not self.start else f"words-start-with/{''.join(self.start)}/"
        end_with = '' if not self.end else f"words-end-in/{''.join(self.end)}/"
        contains = '' if not self.substring else f"words-contain/{''.join(self.substring)}/"
        length = '' if not self.length else f"length/{self.length}/"
        exclude = '' if not self.exclude else f"exclude-letters/{''.join(self.exclude)}/"
        include = '' if not self.include else f"include-letters/{''.join(self.include)}/"
        self.url = self.base_url + start_with + end_with + contains + length + exclude + include

    def grab_words(self, ) -> None:
        """Grabs words from wordfinderx.com"""
        response = requests.get(self.url)

        self.words = []

    def filter_words(self, ) -> None:
        """Filters the words based on user input"""
        pass

    def next_suggestion(self, ):
        """Provides the next suggestions"""
        self.process_letters_for_url()
        self.create_url()
        self.grab_words()
        self.filter_words()
        print(self.words)
