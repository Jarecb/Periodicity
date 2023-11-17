from datetime import timedelta


def generate_inserts(set, average):
    number_to_insert = round((set['interval'] / average) + 0.2)
    print(f'.Number of events to insert = {number_to_insert}')
    days_per_split = round(set['interval'] / number_to_insert)
    new_sets = []
    start_date = set['from']
    for i in range(number_to_insert):
        end_date = start_date + timedelta(days=days_per_split)
        if i + 1 == number_to_insert:
            end_date = set['to']
        interval = (end_date - start_date).days
        entry = {"from": start_date, "to": end_date, "interval": interval, "average": 0, "real": False, 'valid': True}
        new_sets.append(entry)
        start_date = end_date
    return new_sets


def fix_gaps(interval_data):
    total = 0
    for interval_set in interval_data:
        total = total + interval_set['interval']
    average = total / len(interval_data)
    for interval_set in interval_data:
        interval = interval_set['interval']
        if interval > (average * 1.5):
            interval_set['valid'] = False
            interval_data.extend(generate_inserts(interval_set, average))
    return interval_data
