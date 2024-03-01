def calculate_interval_average(data):
    sorted_data = sorted(data, key=lambda x: x['to'])
    for i in range(len(sorted_data)):
        pre, mid, post, count = 0, 0, 0, 1
        mid = sorted_data[i]['interval']

        ipre = i - 1
        if ipre >= 0:
            pre = sorted_data[ipre]['interval']
            count += 1

        ipost = i + 1
        if ipost < len(sorted_data):
            post = sorted_data[ipost]['interval']
            count += 1

        average = round((pre + mid + post) / count) if count > 0 else 0
        sorted_data[i]['average'] = average

    return sorted_data
