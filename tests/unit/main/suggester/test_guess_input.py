from unittest import TestCase

from main.suggester.suggest_words import SuggestWords


class TestSuggestWords(TestCase):
    def setUp(self):
        self.suggest_words = SuggestWords(length=5)

    def test_user_input_successful(
        self,
    ):
        pass

    def test_validate_input_successful(
        self,
    ):
        pass

    def test_validate_input_wrong_len(
        self,
    ):
        pass

    def test_validate_input_wrong_states(
        self,
    ):
        pass

    def test_grab_word(self):
        pass

    def tearDown(self) -> None:
        pass
