#! /usr/bin/env python3

import argparse
import logging
import sys
from pathlib import Path
from sensor_io.dht22 import get_current_sensor_value
from file_op.write import add_data_to_log_file
from filters.convert import unix_to_hr_time

PROGRAM_NAME = 'HomeSensors Data Logger'
PROGRAM_VERSION = '0.1'
PROGRAM_DESCRIPTION = 'log data to file'


def _setup_argparser():
    parser = argparse.ArgumentParser(description='{} - {}'.format(PROGRAM_NAME, PROGRAM_DESCRIPTION))
    parser.add_argument('-V', '--version', action='version', version='{} {}'.format(PROGRAM_NAME, PROGRAM_VERSION))
    parser.add_argument('-d', '--debug', action='store_true', default=False, help='print debug messages')
    parser.add_argument('-l', '--log_file', default='home/pi/sensor.log', help='log file location')
    return parser.parse_args()


def _setup_logging(args):
    log_format = logging.Formatter(fmt='[%(asctime)s][%(module)s][%(levelname)s]: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger('')
    if args.debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    console_logger = logging.StreamHandler()
    console_logger.setFormatter(log_format)
    logger.addHandler(console_logger)


if __name__ == '__main__':
    args = _setup_argparser()
    _setup_logging(args)

    current_data = get_current_sensor_value()
    logging.info('{}, Humidity: {0.1f}%, Temperature: {0.1f}°C'.format(unix_to_hr_time(current_data.timestamp), current_data.humidity, current_data.temperature))
    add_data_to_log_file(Path(args.log_file), current_data)

    sys.exit()
