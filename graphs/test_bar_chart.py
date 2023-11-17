from datetime import date
from unittest import TestCase

from graphs.bar_chart import show_interval_bar_chart


class Test(TestCase):
    def test_show_interval_bar_chart(self):
        test_data = [{'from': date(2023, 3, 4), 'to': date(2023, 4, 4), 'interval': 31, 'average': 31, 'real': True,
                      'valid': True},
                     {'from': date(2023, 4, 4), 'to': date(2023, 6, 5), 'interval': 62, 'average': 0, 'real': True,
                      'valid': False},
                     {'from': date(2023, 6, 5), 'to': date(2023, 7, 6), 'interval': 31, 'average': 29, 'real': True,
                      'valid': True},
                     {'from': date(2023, 7, 6), 'to': date(2023, 8, 1), 'interval': 26, 'average': 28, 'real': True,
                      'valid': True},
                     {'from': date(2023, 4, 4), 'to': date(2023, 5, 5), 'interval': 31, 'average': 31, 'real': False,
                      'valid': True},
                     {'from': date(2023, 5, 5), 'to': date(2023, 6, 5), 'interval': 31, 'average': 31, 'real': False,
                      'valid': True}]
        show_interval_bar_chart(test_data)
