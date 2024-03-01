import unittest
from unittest.mock import patch

import user_input as cli


class UserInputTest(unittest.TestCase):
    @patch("builtins.input", side_effect=["test_data.csv"])
    def test_data_file_selection(self, mock_input):
        result = cli.get_data_file_selection()
        self.assertEqual("test_data.csv", result)

    @patch("builtins.input", side_effect=[""])
    def test_data_file_default(self, mock_input):
        result = cli.get_data_file_selection()
        self.assertEqual("RealData/dates.csv", result)

    @patch("builtins.input", side_effect=["Y"])
    def test_data_file_selection_yes(self, mock_input):
        result = cli.get_derive_events_selection()
        self.assertEqual(True, result)

    @patch("builtins.input", side_effect=["N"])
    def test_data_file_selection_no(self, mock_input):
        result = cli.get_derive_events_selection()
        self.assertEqual(False, result)

    @patch("builtins.input", side_effect=[""])
    def test_prediction_period_default(self, mock_input):
        result = cli.get_prediction_period()
        expected = 0
        self.assertEqual(expected, result)

    @patch("builtins.input", side_effect=["3"])
    def test_prediction_period_three(self, mock_input):
        result = cli.get_prediction_period()
        expected = 3
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
