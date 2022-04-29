from unittest import TestCase
from unittest.mock import Mock, patch

from suggester.guess_input import UserInput


class TestSuggestWords(TestCase):
    def setUp(self):
        self.user_input = UserInput()

    def test_user_input_successful_ggbby(self):
        expected_letters = ["D", "E", "A", "L", "T"]
        expected_states = ["g", "g", "b", "b", "y"]

        # Mock the input function
        side_effect = ["dealt", "ggbby"]
        with patch("builtins.input", side_effect=side_effect):
            self.user_input.user_input()
            res = self.user_input.word
            states = [item["state"] for item in res]
            letters = [item["letter"] for item in res]
            self.assertEqual(states, expected_states)
            self.assertEqual(letters, expected_letters)

    def test_user_input_successful_one_g(self):
        expected_letters = ["D", "E", "A", "L", "T"]
        expected_states = ["g", "g", "g", "g", "g"]

        # Mock the input function
        side_effect = ["dealt", "g"]
        with patch("builtins.input", side_effect=side_effect):
            self.user_input.user_input()
            res = self.user_input.word
            states = [item["state"] for item in res]
            letters = [item["letter"] for item in res]
            self.assertEqual(states, expected_states)
            self.assertEqual(letters, expected_letters)

    def test_validate_input_true(self):
        self.user_input.word = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "b"},
            {"letter": "L", "state": "b"},
            {"letter": "T", "state": "y"},
        ]
        self.assertTrue(self.user_input.validate_input())

    def test_validate_input_false_length(self):
        self.user_input.word = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "b"},
            {"letter": "L", "state": "b"},
        ]
        self.assertFalse(self.user_input.validate_input())

    def test_validate_input_false_state(self):
        self.user_input.word = [
            {"letter": "D", "state": "z"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "b"},
            {"letter": "L", "state": "b"},
            {"letter": "T", "state": "y"},
        ]
        self.assertFalse(self.user_input.validate_input())

    def test_get_word_invalid(self):
        self.user_input.user_input = Mock()
        self.user_input.validate_input = Mock(return_value=False)
        self.assertFalse(self.user_input.get_word())

    def tearDown(self) -> None:
        self.user_input = None
