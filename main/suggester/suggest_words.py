import requests
from english_words import english_words_set
from bs4 import BeautifulSoup
from string import digits
import logging


class SuggestWords:
    """This class gets the info on the words.
    Then, suggest a list of words based on the info."""

    def __init__(self, length: int) -> None:
        self.base_url = "https://wordfinderx.com/words-for/_/"
        self.word_list_generated = False
        self.used_dictionary = False
        self.go_use_dictionary = False
        self.letters = []
        self.start = ""
        self.end = ""
        self.substring = ""
        self.length = length
        self.include = []
        self.exclude = []
        self.url = ""
        self.words = []
        self.yellow_letters = {0: [], 1: [], 2: [], 3: [], 4: []}
        self.green_letters = {0: "", 1: "", 2: "", 3: "", 4: ""}
        self.black_letters = []

    def process_letters_for_url(self) -> None:
        """Processes the letters to create the url"""
        # find exclude and include
        for item in self.letters:
            if item["state"] == "b":
                self.exclude.append(item["letter"])
                self.black_letters.append(item["letter"])
            else:
                self.include.append(item["letter"])
        del item
        self.include = sorted(list(set(self.include)))
        self.exclude = sorted(list(set(self.exclude)))

        # find start and end and initiate substring
        if self.letters[0]["state"] == "g":
            self.start = self.letters[0]["letter"]
            if self.letters[1]["state"] == "g":
                self.start += self.letters[1]["letter"]

        if self.letters[-1]["state"] == "g":
            self.end = self.letters[-1]["letter"]
            if self.letters[-2]["state"] == "g":
                self.end = self.letters[-2]["letter"] + self.end

        # find substring
        temp_substring = self.letters[0]["letter"]
        sub_flag = False
        for index in range(1, len(self.letters)):
            current = self.letters[index]
            previous = self.letters[index - 1]
            if (
                current["state"] == "g"
                and previous["state"] != "g"
                and index != self.length - 1
            ):
                sub_flag = True
                temp_substring = current["letter"]
            if current["state"] == "g" and previous["state"] == "g":
                sub_flag = True
                temp_substring += current["letter"]
            else:
                if not sub_flag:
                    sub_flag = False
                    temp_substring = ""

        self.substring = temp_substring if len(temp_substring) > 1 else ""

    def create_url(self) -> None:
        """Creates an url to wordfinderx.com"""
        # if a letter is listed in substring, it should be removed from exclude list.
        # this happens when user wants to check if occurrence of a letter is more than once.
        for letter in self.exclude:
            if letter in self.substring or letter in self.include:
                self.exclude.remove(letter)
        start_with = "" if not self.start else f"words-start-with/{self.start}/"
        end_with = "" if not self.end else f"words-end-in/{self.end}/"
        contains = "" if not self.substring else f"words-contain/{self.substring}/"
        length = "" if not self.length else f"length/{self.length}/"
        exclude = (
            "" if not self.exclude else f"exclude-letters/{''.join(self.exclude)}/"
        )
        include = (
            "" if not self.include else f"include-letters/{''.join(self.include)}/"
        )
        self.url = (
            self.base_url
            + start_with
            + end_with
            + contains
            + length
            + exclude
            + include
        )

    def grab_words_online(self) -> dict:
        """Grabs words from wordfinderx.com"""
        # initiate variables.
        success = False
        words_list = []
        # grab words from the url.
        try:
            response = requests.get(self.url)
            status = response.status_code
            if status == 200:
                page_content = response.content
                soup = BeautifulSoup(page_content, "html.parser")
                words_list = [
                    tag.text.strip().strip(digits).upper()
                    for tag in soup.find_all(
                        "div", {"class": "wordblock word-list-item"}
                    )
                ]
                success = True
        except Exception as error:
            logging.error(f"Error: {error}")

        return {"success": success, "words": words_list}

    def get_words_from_dictionary(self) -> bool:
        """Gets words from the dictionary"""
        # not implemented yet.
        # initiate variables.
        status = False
        # grab words from package.
        try:
            words = []  # get some words. idk how.

            self.used_dictionary = True
        except Exception as error:
            logging.error(f"Error: {error}")
            words = []

        if len(words) > 0:
            self.words = words
            status = True
        else:
            logging.info("Could not provide words from package!")

        return status

    def list_words_online(self) -> None:
        """Provide a lists words"""
        self.process_letters_for_url()
        self.create_url()
        words = self.grab_words_online()
        self.words = words["words"]
        if words["success"] and len(words["words"]) > 0:
            self.word_list_generated = True
        else:
            logging.info("Could not provide words online!")

    def update_place_state(self) -> None:
        """Completes yellow_letters and green_letters dictionaries
        based on the misplaced letters"""
        for index, letter in enumerate(self.letters):
            if letter["state"] == "y":
                self.yellow_letters[index].append(letter["letter"])
            elif letter["state"] == "g":
                self.green_letters[index] = letter["letter"]
            elif letter["state"] == "b":
                self.black_letters.append(letter["letter"])

    def filter_words(self) -> None:
        """Filters the words based on user input"""
        filter_out = []
        for suggestion in self.words:
            remove_flag = False
            for index, letter in enumerate(suggestion):
                # if there is a misplaced yellow letter.
                if suggestion[index] in self.yellow_letters[index]:
                    remove_flag = True
                # if there is a misplaced green letter.
                if self.green_letters[index]:
                    if suggestion[index] != self.green_letters[index]:
                        remove_flag = True
                # if the letter is black.
                if suggestion[index] in self.black_letters and suggestion[
                    index
                ] not in list(self.green_letters.values()):
                    remove_flag = True
                if remove_flag:
                    filter_out.append(suggestion)
                    break
        self.words = [word for word in self.words if word not in filter_out]

    def validate_input(self) -> bool:
        """
        Must check if same place does not have
        more than one kind of state.
        """
        return True

    def next_suggestion(self, letters: list):
        """Provides the next suggestions"""
        self.letters = letters
        # check whether the answer is found.
        found = all(letter["state"] == "g" for letter in self.letters)
        if not found:
            # check whether the guess is valid.
            valid = self.validate_input()
            if valid:
                # check if the list of words is generated or should fetch words online.
                if not self.word_list_generated:
                    self.list_words_online()
                # check if generated list is sufficient or should use the dictionary package.
                if self.go_use_dictionary:
                    self.get_words_from_dictionary()
                # filter the words based on the user input.
                self.update_place_state()
                self.filter_words()
                if len(self.words) > 0:
                    print("Choose one of these:\n" + ", ".join(self.words))
                    return "continue"
                elif not self.used_dictionary:
                    self.used_dictionary = True
                    self.go_use_dictionary = True
                logging.info("Could not provide suggestions!")
                return "out"
            logging.info("The input is not valid. Enter the words again.\n")
            return "invalid"
        logging.info("Word is found.")
        return "found"
