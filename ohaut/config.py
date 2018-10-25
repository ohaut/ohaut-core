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

MQTT_OPTS = [
    cfg.HostnameOpt('server',
               default='localhost',
               help='MQTT server address'),
    cfg.IntOpt('port',
               default=1883,
               help='MQTT server port'),
    cfg.StrOpt('user',
               default=None,
               help='MQTT connection username'),
    cfg.StrOpt('password',
               default=None,
               help='MQTT connection username')]

_conf = None


def get():
    """Load the configuration and return the CONF object."""
    global _conf
    if _conf is None:
        cfg.CONF.register_opts(OPTS)
        cfg.CONF.register_opts(MQTT_OPTS, group='mqtt')
        cfg.CONF(project='ohaut')
        _conf = cfg.CONF
    return _conf
