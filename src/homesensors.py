from flask import Flask
from sensor_io.dht22 import get_current_sensor_value
from filter.convert import unix_to_hr_time


app = Flask(__name__)


@app.route("/")
def home():
    sensor_value = get_current_sensor_value()
    return "{} Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(unix_to_hr_time(sensor_value.timestamp), sensor_value.temperature, sensor_value.humidity)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
