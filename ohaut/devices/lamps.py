from ohaut.devices import device


class ThreeChannelLed(device.Device):

    def __init__(self, device_id, details):
        super(ThreeChannelLed, self).__init__(device_id, details)
        self._update_fields(details)

    def _update_fields(self, details):
        self.enabled_leds = filter(lambda char: char == '1',
                                   "{0:b}".format(int(details.sub_bitmask)))

    def update(self, details):
        super(ThreeChannelLed, self).update(details)
        self._update_fields(details)
