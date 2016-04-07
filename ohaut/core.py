from ohaut import config
from ohaut import mqtt

__version__ = "0.0.1"


def main():
    client = mqtt.MQTTClient()
    client.connect("192.168.1.251", 1883, 60)
    client.loop_forever()
