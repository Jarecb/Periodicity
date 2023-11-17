from datetime import timedelta


def predict_next(data, averaging_periods):
    sorted_data = sorted(data, key=lambda x: x['to'])

    predictions = []
    for i in range(len(sorted_data) + 1):
        step = i - averaging_periods
        total = 0
        count = 0
        for ii in range(step, i):
            if ii >= 0:
                total += sorted_data[ii]['interval']
                count += 1
        if count > 0:
            average = round(total / count)
        else:
            average = 0
        if i >= len(sorted_data):
            prediction = predictions[i - 1]['date'] + timedelta(days=average)
        else:
            prediction = sorted_data[i]['from'] + timedelta(days=average)
        entry = {"date": prediction, "interval": average}
        predictions.append(entry)

    return predictions
