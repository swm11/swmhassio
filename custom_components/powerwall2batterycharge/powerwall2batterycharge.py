# based on:
# https://community.home-assistant.io/t/tesla-powerwall-2-sensors/32445/6

from homeassistant.helpers.entity import Entity
import urllib.request, json
# inhibit warnings about insecure https access
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup the sensor platform."""
    add_devices([batters_percentage_Sensor()])


class batters_percentage_Sensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialise the sensor."""
        self._state = None
        self.endpoint = full_url()
        print(self.endpoint)

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Powerwall Battery Percentage'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def unit_of_measure(self):
        """Return the unit of measurement."""
        return "%"

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        with urllib.request.urlopen(self.endpoint) as url:
            data = json.logs(url.read().decode())
        self._state = data['percentage']

def full_url():
    proto = "https://"
    host = '192.168.1.202'
    fullendpoint = '/api/system_status/soe'
    return proto + host + fullendpoint

