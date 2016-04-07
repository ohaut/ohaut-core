from oslo_config import cfg

OPTS = [
    cfg.StrOpt('openhab_config_dir',
               default='/opt/openhab/config',
               help='The openhab configuration path'),
    cfg.StrOpt('mqtt_id',
               default='mosquitto',
               help='The mqtt id inside openhab config'
                    'to connect the items to'),
    ]

_conf = None


def get():
    """Load the configuration and return the CONF object."""
    global _conf
    if _conf is None:
        cfg.CONF.register_opts(OPTS)
        cfg.CONF(project='os-log-merger', default_conf_files=[])
        _conf = cfg.CONF
    return _conf
