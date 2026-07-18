import csv
import os

class TelemetryLogger:
    def __init__(self, file_path='flight_data.csv'):
        self.file_path = file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def log(self, data_dict):
        write_header = not os.path.exists(self.file_path)
        with open(self.file_path, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data_dict.keys())
            if write_header:
                writer.writeheader()
            writer.writerow(data_dict)