import attrdict
import json

import paho.mqtt.client as mqtt

from ohaut import consts
from ohaut.devices import manager

class MQTTClient(object):

    def __init__(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def connect(self, *args, **kwargs):
        self.client.connect(*args, **kwargs)

    @staticmethod
    def on_connect(client, userdata, rc):
        client.subscribe(consts.OHAUT_SUBS)

    def on_message(self, client, userdata, msg):
        topic_match = consts.TOPIC_RE.match(msg.topic)
        device_id = topic_match.group(1)
        device_end = topic_match.group(2)

        if device_end == consts.DETAILS:
            details = attrdict.AttrDict(
                json.loads(msg.payload.decode('ascii')))
            if 'version' in details:
                manager.handle_device(device_id, details)

        elif device_end == consts.ONLINE:
            if msg.payload == b'1':
                manager.handle_device_online(device_id)
            else:
                manager.handle_device_offline(device_id)

    def loop_forever(self):
        self.client.loop_forever()


