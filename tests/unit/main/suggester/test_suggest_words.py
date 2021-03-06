from unittest import TestCase
from unittest.mock import Mock

from suggester.suggest_words import SuggestWords


class TestSuggestWords(TestCase):
    def setUp(self):
        self.suggest_words = SuggestWords(length=5)

    def test_process_letters_for_url_include_exclude(self):
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

    def test_process_letters_for_url_start_end(self):
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

    def test_process_letters_for_url_substring_ggyyy(self):
        self.suggest_words.letters = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "y"},
            {"letter": "L", "state": "y"},
            {"letter": "T", "state": "y"},
        ]
        self.suggest_words.process_letters_for_url()
        res = self.suggest_words
        self.assertEqual(res.start, "DE")
        self.assertEqual(res.end, "")
        self.assertEqual(res.substring, "DE")
        self.assertEqual(res.exclude, [])
        self.assertEqual(res.include, ["A", "D", "E", "L", "T"])

    def test_process_letters_for_url_substring_ggbbg(self):
        self.suggest_words.letters = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "b"},
            {"letter": "L", "state": "b"},
            {"letter": "T", "state": "g"},
        ]
        self.suggest_words.process_letters_for_url()
        res = self.suggest_words
        self.assertEqual(res.start, "DE")
        self.assertEqual(res.end, "T")
        self.assertEqual(res.substring, "DE")
        self.assertEqual(res.exclude, ["A", "L"])
        self.assertEqual(res.include, ["D", "E", "T"])

    def test_create_url_valid(self):
        self.suggest_words.start = "START"
        self.suggest_words.end = "END"
        self.suggest_words.substring = "SUB"
        self.suggest_words.exclude = ["E", "X", "C", "L", "U", "D", "E"]
        self.suggest_words.include = ["I", "N", "C", "L", "U", "D", "E"]
        self.suggest_words.create_url()

        expected_url = (
            "https://wordfinderx.com/words-for/_/words-start-with/START/"
            "words-end-in/END/words-contain/SUB/length/5/"
            "exclude-letters/XLD/include-letters/INCLUDE/"
        )
        self.assertEqual(self.suggest_words.url, expected_url)
        self.assertEqual(sorted(self.suggest_words.exclude), ["D", "L", "X"])

    def test_grab_words_online_successful_words(self):
        self.suggest_words.url = (
            "https://wordfinderx.com/words-for/_/words-start-with/D/"
            "words-end-in/Y/words-contain/IR/length/5/exclude-letters/SUB/"
            "include-letters/DIRY/"
        )
        expected_words = ["DAIRY", "DIRTY"]
        res = self.suggest_words.grab_words_online()
        self.assertTrue(isinstance(res, dict))
        self.assertEqual(list(res.keys()), ["success", "words"])
        self.assertEqual(res["success"], True)
        self.assertTrue(
            all([True if word in res["words"] else False for word in expected_words])
        )

    def test_grab_words_online_successful_no_words(self):
        self.suggest_words.url = (
            "https://wordfinderx.com/words-for/_/words-start-with/D/"
            "words-end-in/Y/words-contain/IR/length/5/exclude-letters/DIRY/"
            "include-letters/DIRY/"
        )
        res = self.suggest_words.grab_words_online()
        self.assertTrue(isinstance(res, dict))
        self.assertEqual(list(res.keys()), ["success", "words"])
        self.assertEqual(res["success"], True)
        self.assertEqual(res["words"], [])

    def test_grab_words_online_failed_no_url(self):
        self.suggest_words.url = None
        res = self.suggest_words.grab_words_online()
        self.assertTrue(isinstance(res, dict))
        self.assertEqual(list(res.keys()), ["success", "words"])
        self.assertEqual(res["success"], False)
        self.assertEqual(res["words"], [])

        expected_log = "Error: Invalid URL 'None'"
        with self.assertLogs() as captured_log:
            self.suggest_words.grab_words_online()
        self.assertEqual(len(captured_log.records), 1)
        self.assertTrue(captured_log.records[0].getMessage().startswith(expected_log))

    def test_grab_words_online_failed_bad_url(self):
        self.suggest_words.url = "https://wordfinderx.com/XXXXX"
        res = self.suggest_words.grab_words_online()
        self.assertTrue(isinstance(res, dict))
        self.assertEqual(list(res.keys()), ["success", "words"])
        self.assertEqual(res["success"], False)
        self.assertEqual(res["words"], [])

    def test_list_words_from_package(self):  # the function is not implemented yet.
        pass

    def test_list_words_online_successful_with_words(self):
        self.suggest_words.process_letters_for_url = Mock()
        self.suggest_words.create_url = Mock()
        self.suggest_words.grab_words_online = Mock(
            return_value={"success": True, "words": ["DAIRY", "DIRTY"]}
        )
        self.suggest_words.list_words_online()
        res = self.suggest_words.words
        self.assertTrue(isinstance(res, list))
        self.assertEqual(res, ["DAIRY", "DIRTY"])
        self.assertEqual(self.suggest_words.word_list_generated, True)

    def test_list_words_online_successful_no_words(self):
        self.suggest_words.process_letters_for_url = Mock()
        self.suggest_words.create_url = Mock()
        self.suggest_words.grab_words_online = Mock(
            return_value={"success": True, "words": []}
        )
        self.suggest_words.list_words_online()

        expected_log = "Could not provide words online!"
        with self.assertLogs() as captured_log:
            self.suggest_words.list_words_online()
        self.assertEqual(len(captured_log.records), 1)
        self.assertEqual(captured_log.records[0].getMessage(), expected_log)

    def test_list_words_online_failed(self):
        self.suggest_words.process_letters_for_url = Mock()
        self.suggest_words.create_url = Mock()
        self.suggest_words.grab_words_online = Mock(
            return_value={"success": False, "words": []}
        )
        self.suggest_words.list_words_online()

        expected_log = "Could not provide words online!"
        with self.assertLogs() as captured_log:
            self.suggest_words.list_words_online()
        self.assertEqual(len(captured_log.records), 1)
        self.assertEqual(captured_log.records[0].getMessage(), expected_log)

    def test_update_place_state(self):
        self.suggest_words.letters = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "b"},
            {"letter": "L", "state": "y"},
            {"letter": "T", "state": "y"},
        ]
        expected_yellow = {0: [], 1: [], 2: [], 3: ["L"], 4: ["T"]}
        expected_green = {0: "D", 1: "E", 2: "", 3: "", 4: ""}
        expected_black = ["A"]

        self.suggest_words.update_place_state()
        yellow = self.suggest_words.yellow_letters
        green = self.suggest_words.green_letters
        black = self.suggest_words.black_letters
        self.assertEqual(yellow, expected_yellow)
        self.assertEqual(green, expected_green)
        self.assertEqual(black, expected_black)
        black_in_green = all(
            [False if letter in black else True for letter in green.values()]
        )
        self.assertTrue(black_in_green)
        black_in_yellow = all(
            [False if letter in black else True for letter in yellow.values()]
        )
        self.assertTrue(black_in_yellow)

    def test_filter_words(self):
        self.suggest_words.words = [
            "DAIRY",
            "DIRTY",
            "DUMBO",
            "DESERT",
            "DODGE",
            "DUCKS",
        ]
        self.suggest_words.yellow_letters = {
            0: [],
            1: ["U", "E"],
            2: ["D", "R"],
            3: ["L"],
            4: ["T"],
        }
        self.suggest_words.green_letters = {0: "D", 1: "", 2: "", 3: "", 4: "Y"}

        self.suggest_words.filter_words()
        res = self.suggest_words.words
        self.assertTrue(isinstance(res, list))
        self.assertEqual(res, ["DAIRY"])

    def test_validate_input_valid(self):  # the function is not implemented yet.
        pass

    def test_validate_input_invalid(self):  # the function is not implemented yet.
        pass

    def test_found(self):
        letters = [
            {"letter": "D", "state": "g"},
            {"letter": "E", "state": "g"},
            {"letter": "A", "state": "g"},
            {"letter": "L", "state": "g"},
            {"letter": "T", "state": "g"},
        ]
        res = self.suggest_words.next_suggestion(letters=letters)
        self.assertTrue(isinstance(res, str))
        self.assertEqual(res, "found")

        expected_log = "Word is found."
        with self.assertLogs() as captured_log:
            self.suggest_words.next_suggestion(letters=letters)
        self.assertEqual(len(captured_log.records), 1)
        self.assertEqual(captured_log.records[0].getMessage(), expected_log)

    def tearDown(self) -> None:
        self.suggest_words = None
