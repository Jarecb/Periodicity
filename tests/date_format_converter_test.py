import unittest
from datetime import date

import date_format_converter as dfc


class DateFormatConverterTest(unittest.TestCase):
    def test_list_conversion_from_str_to_date_objects(self):
        test_data = ["21/10/2023", "06/07/2023", "26/09/2023"]
        expected = [date(2023, 10, 21), date(2023, 7, 6), date(2023, 9, 26)]
        result = dfc.date_format_converter(test_data)
        self.assertEqual(expected, result)

    def test_sorting_of_dates(self):
        test_data = [date(2023, 10, 21), date(2023, 7, 6), date(2023, 9, 26)]
        expected = [date(2023, 7, 6), date(2023, 9, 26), date(2023, 10, 21)]
        result = dfc.sort_dates(test_data)
        self.assertEqual(expected, result)

    def test_create_dict_of_intervals(self):
        test_data = [date(2023, 7, 6), date(2023, 9, 26), date(2023, 10, 21)]
        expected = [{"from": date(2023, 7, 6), "to": date(2023, 9, 26), "interval": 82, "average": 0, "real": True,
                     'valid': True},
                    {"from": date(2023, 9, 26), "to": date(2023, 10, 21), "interval": 25, "average": 0, "real": True,
                     'valid': True}]
        result = dfc.calculate_interval(test_data)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
