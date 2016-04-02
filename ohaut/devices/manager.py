
from ohaut.devices import lamps
from ohaut import exceptions


CLASS_MAP = {'3CHANLED': lamps.ThreeChannelLed}


class DeviceManager(object):

    _instance = None

    def __init__(self):
        self._devices = {}
        self._online = {}

    @classmethod
    def get_instance(cls):
        #NOTE(mangelajo): consider locking
        if cls._instance is None:
            cls._instance = DeviceManager()
        return cls._instance

    def get_device(self, device_id):
        return self._devices.get(device_id, None)

    def create_device(self, device_id, details):
        device_class = CLASS_MAP[details.type]
        device = device_class(device_id, details)
        self._devices[device_id] = device

        online_status = self._online.get(device_id, None)
        if online_status is True:
            device.go_online()
            self._online.pop(device_id)
        elif online_status is False:
            device.go_offline()
            self._online.pop(device_id)

        print(self._devices)

    def handle_device_details(self, device_id, details):
        device = self.get_device(device_id)
        if device:
            try:
                device.update(details)
            except exceptions.InvalidDeviceType:
                self.create_device(device_id, details)
        else:
            self.create_device(device_id, details)

    def handle_device_online(self, device_id):
        device = self.get_device(device_id)
        if device:
            device.go_online()
        else:
            self._online[device_id] = True

    def handle_device_offline(self, device_id):
        device = self.get_device(device_id)
        if device:
            device.go_offline()
        else:
            self._online[device_id] = False


def handle_device(device_id, details):
    device_manager = DeviceManager.get_instance()
    device_manager.handle_device_details(device_id, details)


def handle_device_online(device_id):
    device_manager = DeviceManager.get_instance()
    device_manager.handle_device_online(device_id)


def handle_device_offline(device_id):
    device_manager = DeviceManager.get_instance()
    device_manager.handle_device_offline(device_id)
