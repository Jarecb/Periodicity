import interpreter.date_format_converter as fc
from analysis.gap_analysis import fix_gaps
from cli.user_input import get_data_file_selection
from fio.loader import read_data_file
from graphs.bar_chart import show_interval_bar_chart

SEPARATOR = "========================================"


def load_flow():
    print(SEPARATOR)
    # Load dates file
    data_file = get_data_file_selection()
    print('.Loading data')
    raw_data = read_data_file(data_file)
    print('..Converting dates')
    converted_data = fc.date_format_converter(raw_data)
    print('...Sorting Dates')
    sorted_dates = fc.sort_dates(converted_data)
    print('....Calculating Intervals')
    intervals = fc.calculate_interval(sorted_dates)
    print('Data processed')
    print(SEPARATOR)
    # Derive missing dates
    intervals = fix_gaps(intervals)
    print(SEPARATOR)
    show_interval_bar_chart(intervals)
