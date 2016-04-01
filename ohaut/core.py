import json

import paho.mqtt.client as mqtt


__version__ = "0.0.1"


class MQTTClient(object):

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self, *args, **kwargs):
        self.client.connect(*args, **kwargs)

    @staticmethod
    def on_connect(client, userdata, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("/ohaut/#")

    def on_message(self, client, userdata, msg):
        print(msg.topic+" "+str(msg.payload))
        if msg.topic.endswith('/details'):
            print(json.loads(msg.payload.decode('ascii')))

    def loop_forever(self):
        self.client.loop_forever()


def main():
    client = MQTTClient()
    client.connect("192.168.1.251", 1883, 60)
    client.loop_forever()
