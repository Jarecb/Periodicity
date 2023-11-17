import unittest
from unittest.mock import patch

import user_input as cli


class UserInputTest(unittest.TestCase):
    @patch("builtins.input", side_effect=["test_data.csv"])
    def test_data_file_selection(self, mock_input):
        result = cli.get_data_file_selection()
        self.assertEqual(result, "test_data.csv")

    @patch("builtins.input", side_effect=["Y"])
    def test_data_file_selection_yes(self, mock_input):
        result = cli.get_derive_events_selection()
        self.assertEqual(result, True)

    @patch("builtins.input", side_effect=["N"])
    def test_data_file_selection_no(self, mock_input):
        result = cli.get_derive_events_selection()
        self.assertEqual(result, False)

    @patch("builtins.input", side_effect=[""])
    def test_prediction_period_default(self, mock_input):
        result = cli.get_prediction_period()
        expected = 4
        self.assertEqual(result, expected)

    @patch("builtins.input", side_effect=["3"])
    def test_prediction_period_three(self, mock_input):
        result = cli.get_prediction_period()
        expected = 3
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
