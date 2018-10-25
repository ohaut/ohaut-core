import os.path

from ohaut import config
from ohaut import managed_file


class OpenHab(object):
    def __init__(self):
        self._cfg_dir = config.get().openhab_config_dir

    def room_sitemap(self, room):
        path = os.path.join(self._cfg_dir,
                            'configurations',
                            'sitemaps',
                            "{}.sitemap".format(room))
        return managed_file.ManagedFile(path)

    def items(self):
        path = os.path.join(self._cfg_dir,
                            'configurations',
                            'items',
                            'ohaut.items')
        return managed_file.ManagedFile(path)
