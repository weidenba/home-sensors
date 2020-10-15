from pathlib import Path
import logging


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
        for i in range(len(raw_data)):
            raw_data[i] = int(raw_data[i])
        log_data.append(raw_data)
    return log_data
