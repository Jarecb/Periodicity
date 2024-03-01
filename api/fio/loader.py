import json
import os


# Loads date lists from CSV or JSON format files
def read_data_file(data_file):
    if os.path.exists(data_file):
        with open(data_file) as data:
            if data_file.endswith('.csv'):
                return data.read().split(",")
            elif data_file.endswith('.json'):
                json_data = json.load(data)
                return [item["date"] for item in json_data]
    return None
