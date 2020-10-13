import Adafruit_DHT
from collections import namedtuple


DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

SensorValue = namedtuple('SensorValue', ['humidity', 'temperature'])

def get_current_sensor_value():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    return SensorValue(humidity, temperature)
