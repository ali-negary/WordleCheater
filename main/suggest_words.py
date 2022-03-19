import requests
from english_words import english_words_set
from bs4 import BeautifulSoup
from string import digits


class SuggestWords:
    """This class gets the info on the words.
    Then, suggest a list of words based on the info."""

    def __init__(self, letters: list, length: int) -> None:
        self.base_url = 'https://wordfinderx.com/words-for/_/'
        self.letters = letters
        self.start = ''
        self.end = ''
        self.substring = ''
        self.length = length
        self.include = ''
        self.exclude = ''
        self.url = ''
        self.words = []
        self.yellow_letters = {0: [], 1: [], 2: [], 3: [], 4: []}

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

    def grab_words_online(self, ) -> dict:
        """Grabs words from wordfinderx.com"""
        # initiate variables.
        status = False
        words_list = []
        # grab words from the url.
        response = requests.get(self.url)
        status = response.status_code
        if status == 200:
            page_content = response.content
            soup = BeautifulSoup(page_content, 'html.parser')
            words_list = [
                tag.text.strip().strip(digits) for tag in
                soup.find_all('div', {"class": "wordblock word-list-item"})
            ]
            status = True

        return {'status': status, 'words': words_list}

    def get_words_from_dictionary(self) -> dict:
        """Gets words from the dictionary"""
        # initiate variables.
        status = False
        words_list = []
        # grab words from url.

        return {'status': status, 'words': words_list}

    def list_words(self, ):
        """Provide a lists words"""
        words = self.grab_words_online()
        if words['status']:
            self.words = words['words']
        else:
            raise Exception('Could not get words')
            # words = self.get_words_from_dictionary()
            # if words['status']:
            #     self.words = words['words']

    def misplaced_words(self, ):
        """Completes yellow_letters dict based on the misplaced letters"""
        for index, letter in enumerate(self.letters):
            if letter['state'] == 'y':
                self.yellow_letters[index].append(letter['letter'])

    def filter_words(self, ) -> None:
        """Filters the words based on user input"""
        for suggestion in self.words:
            for index, letter in enumerate(suggestion):
                if suggestion[index] in self.yellow_letters[index]:
                    self.words.remove(suggestion)
                    break
            t = 'test'

    def next_suggestion(self, ):
        """Provides the next suggestions"""
        self.process_letters_for_url()
        self.create_url()
        self.list_words()
        self.misplaced_words()
        self.filter_words()
        print(self.words)
