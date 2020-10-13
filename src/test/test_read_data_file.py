import pytest
from file_op.read import convert_data

@pytest.mark.parametrize('log_data, expected_result', [
    (list(), list()),
    (['123;1;2'], [[123,1,2]]),
])
def test_convert_data(log_data, expected_result):
    assert convert_data(log_data) == expected_result
