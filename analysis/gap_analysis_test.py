import unittest
from datetime import date

from analysis.gap_analysis import fix_gaps, generate_inserts


class GapAnalysisTest(unittest.TestCase):
    def test_for_missing_dates(self):
        test_date = [{'from': date(2023, 3, 4), 'to': date(2023, 4, 4), 'interval': 31, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 4, 4), 'to': date(2023, 6, 5), 'interval': 62, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 6, 5), 'to': date(2023, 7, 6), 'interval': 31, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 7, 6), 'to': date(2023, 8, 1), 'interval': 26, 'average': 0, 'real': True,
                      'valid': True}]
        expected = [{'from': date(2023, 3, 4), 'to': date(2023, 4, 4), 'interval': 31, 'average': 0, 'real': True,
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
        result = fix_gaps(test_date)
        self.assertEqual(result, expected)

    def test_insert_generation(self):
        test_data = {'from': date(2023, 4, 4), 'to': date(2023, 7, 5), 'interval': 92, 'average': 0, 'real': True,
                     'valid': True}
        average = 37.5
        expected = [{'from': date(2023, 4, 4), 'to': date(2023, 5, 5), 'interval': 31, 'average': 0, 'real': False,
                     'valid': True},
                    {'from': date(2023, 5, 5), 'to': date(2023, 6, 5), 'interval': 31, 'average': 0, 'real': False,
                     'valid': True},
                    {'from': date(2023, 6, 5), 'to': date(2023, 7, 5), 'interval': 30, 'average': 0, 'real': False,
                     'valid': True}]
        result = generate_inserts(test_data, average)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
