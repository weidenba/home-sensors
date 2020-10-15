from tempfile import TemporaryDirectory
from pathlib import Path
from file_op.write import add_data_to_log_file
from file_op.read import read_data, convert_data
from collections import namedtuple

SensorValue = namedtuple('SensorValue', ['timestamp', 'humidity', 'temperature'])


def test_add_data_to_log():
    test_log_data = SensorValue(123, 2, 3)
    test_dir = TemporaryDirectory()
    test_file = Path(test_dir.name, 'test.log')
    add_data_to_log_file(test_file, test_log_data)
    add_data_to_log_file(test_file, test_log_data)
    result = read_data(test_file)
    result = convert_data(result)
    assert len(result) == 2
    assert result[0] == [123, 2, 3]
    assert result[1] == [123, 2, 3]
