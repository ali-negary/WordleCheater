from unittest import TestCase

from suggester.suggest_words import SuggestWords


class TestSuggestWords(TestCase):
    def setUp(self):
        self.suggest_words = SuggestWords(length=5)

    def test_process_letters_for_url_include_exclude(
        self,
    ):
        self.suggest_words.letters = [
            {"letter": "D", "state": "y"},
            {"letter": "E", "state": "b"},
            {"letter": "A", "state": "y"},
            {"letter": "L", "state": "g"},
            {"letter": "T", "state": "b"},
        ]
        self.suggest_words.process_letters_for_url()
        res = self.suggest_words
        self.assertEqual(res.start, "")
        self.assertEqual(res.end, "")
        self.assertEqual(res.substring, "")
        self.assertEqual(res.exclude, ["E", "T"])
        self.assertEqual(res.include, ["A", "D", "L"])

    def test_process_letters_for_url_start_end(
        self,
    ):
        self.suggest_words.letters = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "b"},
            {"letter": "A", "state": "y"},
            {"letter": "L", "state": "b"},
            {"letter": "T", "state": "g"},
        ]
        self.suggest_words.process_letters_for_url()
        res = self.suggest_words
        self.assertEqual(res.start, "D")
        self.assertEqual(res.end, "T")
        self.assertEqual(res.substring, "")
        self.assertEqual(res.exclude, ["E", "L"])
        self.assertEqual(res.include, ["A", "D", "T"])

    def test_process_letters_for_url_substring(
        self,
    ):
        self.suggest_words.letters = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "y"},
            {"letter": "L", "state": "y"},
            {"letter": "T", "state": "y"},
        ]
        self.suggest_words.process_letters_for_url()
        res = self.suggest_words
        self.assertEqual(res.start, "D")
        self.assertEqual(res.end, "")
        self.assertEqual(res.substring, "DE")
        self.assertEqual(res.exclude, [])
        self.assertEqual(res.include, ["A", "D", "E", "L", "T"])

    # def test_process_letters_for_url_two_substrings(self,):
    #     pass

    def test_create_url_valid(
        self,
    ):
        pass

    def test_create_url_invalid(
        self,
    ):
        """Should test the result when all the parameters are empty."""
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

    def test_found(
        self,
    ):
        pass

    def tearDown(self) -> None:
        pass
