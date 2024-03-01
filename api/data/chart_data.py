from collections import namedtuple

ChartDataBlock = namedtuple('ChartDataBlock',
                            ['labels', 'intervals', 'derived', 'predicted', 'average', 'prediction', 'median'])


def create_data_block():
    return ChartDataBlock(
        get_labels(),
        get_intervals(),
        get_derived(),
        get_predicted(),
        get_average(),
        get_prediction(),
        get_median()
    )


def get_labels():
    return ['01/01/2024', '15/01/2024', '02/03/2024', '10/04/2024']


def get_intervals():
    return [5, 0, 7, 0]


def get_derived():
    return [0, 4, 0, 0]


def get_predicted():
    return [0, 0, 0, 6]


def get_average():
    return [3, 5, 6, 5]


def get_prediction():
    return [5, 6, 7, 5]


def get_median():
    return [2, 2, 5, 5]
