import unittest

import loader as ld


class DataFileLoaderTest(unittest.TestCase):
    def test_if_returns_none_if_file_does_not_exist(self):
        test_file = "test_data.missing"
        result = ld.read_data_file(test_file)
        self.assertEqual(result, None)

    def test_if_csv_file_readable(self):
        test_file = "test_data.csv"
        expected = ["21/10/2023", "06/07/2023", "26/09/2023", "27/08/2023", "01/08/2023", "05/06/2023"]
        result = ld.read_data_file(test_file)
        self.assertListEqual(result, expected)

    def test_if_json_file_readable(self):
        test_file = "test_data.json"
        expected = ["21/10/2023", "06/07/2023", "26/09/2023", "27/08/2023", "01/08/2023", "05/06/2023"]
        result = ld.read_data_file(test_file)
        self.assertListEqual(result, expected)

    def test_if_not_correct_file_format(self):
        test_file = "test_data.bad"
        result = ld.read_data_file(test_file)
        self.assertEqual(result, None)


if __name__ == '__main__':
    unittest.main()
