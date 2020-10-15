from flask import Flask
from sensor_io.dht22 import get_current_sensor_value
from filters.convert import unix_to_hr_time


app = Flask(__name__)


@app.route("/")
def home():
    sensor_value = get_current_sensor_value()
    return render_template('current.html', timestamp=unix_to_hr_time(sensor_value.timestamp), humdity=sensor_value.humidity, temperature=sensor_value.temperature)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
