import Adafruit_DHT
import time
from collections import namedtuple


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

SensorValue = namedtuple('SensorValue', ['timestamp', 'humidity', 'temperature'])


def get_current_sensor_value():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    timestamp = time.time()
    return SensorValue(timestamp, humidity, temperature)
