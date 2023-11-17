from matplotlib import pyplot as plt

from analysis.averaging import calculate_interval_average
from analysis.prediction import predict_next
from cli.user_input import get_derive_events_selection, get_prediction_period


def show_interval_bar_chart(interval_data):
    while True:
        show_derived = get_derive_events_selection()
        if show_derived:
            valid_data = [set for set in interval_data if set['valid']]
            valid_data = calculate_interval_average(valid_data)
            draw_chart(valid_data)
        else:
            valid_data = [set for set in interval_data if set['real']]
            valid_data = calculate_interval_average(valid_data)
            draw_chart(valid_data)


def add_prediction(sorted_data):
    prediction_period = get_prediction_period()
    prediction_set = predict_next(sorted_data, prediction_period)
    predictions = [set['interval'] for set in prediction_set]
    prediction = prediction_set[-1]
    from_date = sorted_data[-1]['to']
    prediction_entry = {"from": from_date, "to": prediction['date'], "interval": prediction['interval'],
                        "average": 0,
                        "real": False,
                        'valid': False}
    sorted_data.append(prediction_entry)
    return sorted_data, predictions, prediction_period


def draw_chart(valid_data):
    sorted_data = sorted(valid_data, key=lambda x: x['to'])
    sorted_data, predictions, prediction_period = add_prediction(sorted_data)
    averages = [set['average'] for set in sorted_data]
    real = [set['interval'] if set['real'] else 0 for set in sorted_data]
    predicted = [set['interval'] if not set['real'] and not set['valid'] else 0 for set in sorted_data]
    derived = [set['interval'] if not set['real'] and set['valid'] else 0 for set in sorted_data]
    plt.bar(range(len(real)), real, color='green', label='Dates')
    plt.bar(range(len(predicted)), predicted, color='cyan', label='Next Prediction')
    plt.bar(range(len(derived)), derived, color='red', label='Derived Dates')
    plt.plot(averages, color='black', label='Average')
    plt.plot(predictions, color='blue', label='Prediction Fit')
    plt.suptitle('Periodicity', y=1, fontsize=18)
    plt.title(f'{prediction_period} interval prediction', fontsize=10)
    plt.xlabel('Date')
    plt.ylabel('Interval')
    dates = [set['to'] for set in sorted_data]
    formatted_dates = [d.strftime('%d/%m') for d in dates]
    plt.xticks(range(len(dates)), formatted_dates)
    plt.legend(fancybox=True, shadow=True, loc='lower left')
    plt.show()
