from unittest import TestCase

from main.suggester.suggest_words import SuggestWords


class TestSuggestWords(TestCase):
    def setUp(self):
        self.suggest_words = SuggestWords(length=5)

    def test_process_letters_for_url_include_exclude(
        self,
    ):
        pass

    def test_process_letters_for_url_start_end(
        self,
    ):
        pass

    def test_process_letters_for_url_substring(self):
        pass

    def test_create_url(
        self,
    ):
        pass

    def test_grab_words_online_successful(
        self,
    ):
        pass

    def test_grab_words_online_failure(
        self,
    ):
        pass

    def test_list_words_from_online(
        self,
    ):
        pass

    def test_list_words_from_package(
        self,
    ):  # the function is not implemented yet.
        pass

    def test_place_state(
        self,
    ):
        pass

    def test_filter_words(
        self,
    ):
        pass

    def test_validate_input_valid(
        self,
    ):  # the function is not implemented yet.
        pass

    def test_validate_input_invalid(
        self,
    ):  # the function is not implemented yet.
        pass

    def tearDown(self) -> None:
        pass
