import unittest
from datetime import date

from analysis.averaging import calculate_interval_average


class TestThreeEntryAveraging(unittest.TestCase):
    def test_three_entry_average(self):
        test_data = [{'from': date(2023, 3, 4), 'to': date(2023, 4, 4), 'interval': 31, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 4, 4), 'to': date(2023, 6, 5), 'interval': 62, 'average': 0, 'real': True,
                      'valid': False},
                     {'from': date(2023, 6, 5), 'to': date(2023, 7, 6), 'interval': 31, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 7, 6), 'to': date(2023, 8, 1), 'interval': 26, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 4, 4), 'to': date(2023, 5, 5), 'interval': 31, 'average': 0, 'real': False,
                      'valid': True},
                     {'from': date(2023, 5, 5), 'to': date(2023, 6, 5), 'interval': 31, 'average': 0, 'real': False,
                      'valid': True}]
        expected = [{'from': date(2023, 3, 4), 'to': date(2023, 4, 4), 'interval': 31, 'average': 31, 'real': True,
                     'valid': True},
                    {'from': date(2023, 4, 4), 'to': date(2023, 5, 5), 'interval': 31, 'average': 41, 'real': False,
                     'valid': True},
                    {'from': date(2023, 4, 4), 'to': date(2023, 6, 5), 'interval': 62, 'average': 41, 'real': True,
                     'valid': False},
                    {'from': date(2023, 5, 5), 'to': date(2023, 6, 5), 'interval': 31, 'average': 41, 'real': False,
                     'valid': True},
                    {'from': date(2023, 6, 5), 'to': date(2023, 7, 6), 'interval': 31, 'average': 29, 'real': True,
                     'valid': True},
                    {'from': date(2023, 7, 6), 'to': date(2023, 8, 1), 'interval': 26, 'average': 28, 'real': True,
                     'valid': True}]

        result = calculate_interval_average(test_data)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
