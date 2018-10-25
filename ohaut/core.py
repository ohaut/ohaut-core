from ohaut import config
from ohaut import mqtt

__version__ = "0.0.1"


def main():
    cfg = config.get()
    client = mqtt.MQTTClient()
    client.connect(cfg.mqtt.server, cfg.mqtt.port, 60)
    client.loop_forever()
