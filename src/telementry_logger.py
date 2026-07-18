import csv

class TelemetryLogger:
    def log(self, data_dict):
        with open('flight_data.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=data_dict.keys())
            writer.writerow(data_dict)