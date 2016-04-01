OHAUT-Core onboarding subsystem
===============================

This subsystem is the central piece, but still optional, for a complete
ohaut deployment. It's purpose is finding new deployed devices, listing them
and registering them into the home automation frontend (currently OpenHab).

Discovery of the devices
~~~~~~~~~~~~~~~~~~~~~~~~

The devices are discovered in the MQTT bus over the /ohaut/# path.

Any compliant device should register itself as  (preliminar):

.. code::

    /ohaut/<device_id>/online = 1
    /ohaut/<device_id>/details = {"version": "0",
                                  "name": "Lamp",
                                  "type": "3CHANLED",
                                  "has_sitemap" : "0",
                                  "has_rules": "0",
                                  "order": "0",
                                  "section": "",
                                  "room": "Default",
                                  "mqtt_path": "/home/default/lamp",
                                  "sub_bitmask": "0003"}

