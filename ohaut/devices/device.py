from ohaut import exceptions

class Device(object):

    def __init__(self, device_id, details):
        self.device_id = device_id
        self.type = details.type
        self._update_generic_fields(details)

    def _update_generic_fields(self, details):
        self.room = details.room
        self.order = details.order
        self.name = details.name
        self.ip = details.ip
        self.has_sitemap = details.has_sitemap
        self.has_rules = details.has_rules

    def go_offline(self):
        print(self, 'gone offline') 

    def go_online(self):
        print(self, 'gone online')

    def update(self, details):
        if self.type != details.type:
            raise exceptions.InvalidDeviceType()
        self._update_generic_fields(details)
