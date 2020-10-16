from flask import Flask, render_template
from sensor_io.dht22 import get_current_sensor_value
from filters.convert import unix_to_hr_time
from pathlib import Path
from file_op.read import read_data, convert_data

app = Flask(__name__)


@app.route("/debug")
def home():
    sensor_value = get_current_sensor_value()
    return render_template('current.html', timestamp=unix_to_hr_time(sensor_value.timestamp), humidity=sensor_value.humidity, temperature=sensor_value.temperature)

@app.route("/")
def history():
    sensor_value = get_current_sensor_value()

    log_file_path = Path('/home/pi/sensor.log')
    history_data = read_data(log_file_path)
    history_data = convert_data(history_data)
    return render_template('history.html', data=history_data, current_sensor_data=sensor_value, timestamp=unix_to_hr_time(sensor_value.timestamp))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
