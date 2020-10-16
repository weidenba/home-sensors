from pathlib import Path
import logging
from filters.convert import unix_to_hr_time


def read_data(file_path: Path) -> list:
    try:
        with open(file_path, 'r') as data_file:
            log_entries = data_file.readlines()
        return log_entries
    except Exception as e:
        logging.error('Could not read file!')


def convert_data(log_entries: list) -> list:
    log_data = list()
    for entry in log_entries:
        raw_data = entry.split(';')
        raw_data[0] = unix_to_hr_time(float(raw_data[0]))
        raw_data[1] = float(raw_data[1])
        raw_data[2] = float(raw_data[2])
        log_data.append(raw_data)
    return log_data
