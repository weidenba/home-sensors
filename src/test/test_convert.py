from filter.convert import unix_to_hr_time


def test_unix_to_hr_time():
    assert unix_to_hr_time(1602775017.5075128) == '2020-10-15 17:16:57'
