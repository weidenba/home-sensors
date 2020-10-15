from pathlib import Path
import logging


def add_data_to_log_file(file_path: Path, sensor_values):
    log_data_line = '{};{};{}\n'.format(sensor_values.timestamp, sensor_values.humidity, sensor_values.temperature)
    try:
        with open(file_path, 'a') as log_file:
            log_file.write(log_data_line)
    except Exception:
        logging.error('Could not add log data to file')
