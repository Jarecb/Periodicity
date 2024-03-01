import unittest
from datetime import date

from analysis.prediction import predict_next


class TestPredictionOfFutureEvents(unittest.TestCase):
    def test_predict_next(self):
        test_data = [{'from': date(2023, 5, 2), 'to': date(2023, 6, 5), 'interval': 34, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 6, 5), 'to': date(2023, 7, 6), 'interval': 31, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 7, 6), 'to': date(2023, 8, 1), 'interval': 26, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 8, 1), 'to': date(2023, 8, 27), 'interval': 26, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 8, 27), 'to': date(2023, 9, 26), 'interval': 30, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 9, 26), 'to': date(2023, 10, 21), 'interval': 25, 'average': 0, 'real': True,
                      'valid': True},
                     {'from': date(2023, 10, 21), 'to': date(2023, 11, 5), 'interval': 15, 'average': 0, 'real': True,
                      'valid': True}]
        expected = [{'date': date(2023, 5, 2), 'interval': 0},
                    {'date': date(2023, 7, 9), 'interval': 34},
                    {'date': date(2023, 8, 7), 'interval': 32},
                    {'date': date(2023, 8, 31), 'interval': 30},
                    {'date': date(2023, 9, 25), 'interval': 29},
                    {'date': date(2023, 10, 24), 'interval': 28},
                    {'date': date(2023, 11, 17), 'interval': 27},
                    {'date': date(2023, 12, 11), 'interval': 24}]
        averaging_periods = 4
        result = predict_next(test_data, averaging_periods)
        self.assertEqual(result, expected)

        if __name__ == '__main__':
            unittest.main()
