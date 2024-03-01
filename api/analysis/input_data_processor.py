from datetime import datetime


def date_format_converter(date_string):
    date_format = "%d/%m/%Y"
    return [datetime.strptime(date_str, date_format).date() for date_str in date_string]


def sort_dates(unsorted_list):
    return sorted(unsorted_list)


def calculate_interval(dates_list):
    intervals = []

    for i in range(len(dates_list) - 1):
        interval = (dates_list[i + 1] - dates_list[i]).days
        entry = {"from": dates_list[i], "to": dates_list[i + 1], "interval": interval, "average": 0, "real": True,
                 'valid': True}
        intervals.append(entry)

    return intervals
