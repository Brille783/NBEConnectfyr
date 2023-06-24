from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity, 
    SensorStateClass,
)
from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from .protocol import Proxy
from .const import DOMAIN
from .rtbdata import RTBData
from logging import getLogger

_LOGGER = getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up the NBE-RTB sensors."""
    _LOGGER.info("This is debugging from sensor.py")
    
    
    #DataUpdateCoordinator 
    dc = hass.data[DOMAIN][entry.entry_id+'_coordinator']

    async_add_entities([
        RTBBinarySensor(dc, 'Boiler Running', 'operating_data/power_pct', BinarySensorDeviceClass.HEAT),
        RTBBinarySensor(dc, 'Boiler Alarm', 'operating_data/off_on_alarm', BinarySensorDeviceClass.PROBLEM),
        RTBSensor(dc, 'Boiler Temperature', 'operating_data/boiler_temp', SensorDeviceClass.TEMPERATURE),
        RTBSensor(dc, 'DWH Temperature', 'operating_data/sun_dhw_temp', SensorDeviceClass.TEMPERATURE),
        RTBSensor(dc, 'External Temperature', 'operating_data/external_temp', SensorDeviceClass.TEMPERATURE),
        RTBSensor(dc, 'Boiler Effect', 'operating_data/power_kw', SensorDeviceClass.POWER),
        RTBSensor(dc, 'Total Consumption', 'consumption_data/counter', SensorStateClass.TOTAL_INCREASING), # state class STATE_CLASS_TOTAL_INCREASING
    ])
    _LOGGER.info(f"Sensor.py, sensors where added!")


class RTBSensor(CoordinatorEntity, SensorEntity):
    """Representation of an RTB sensor."""

    def __init__(self, coordinator, name, client_key, device_class):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.client_key = client_key
        self._device_class = device_class
        self.sensorname = name

    @property
    def name(self):
        """Return the name of the sensor."""
        #_LOGGER.info(f"sensor.py (name) returning \"NBE {self.sensorname}\"")
        return f"NBE {self.sensorname}"

    @property
    def state(self):
        """Return the state of the sensor."""
        state = self.coordinator.rtbdata.get(self.client_key)
        #_LOGGER.info(f"Sensor.py RTBSensor (state) returning \"{state}\"")
        return state

    @property
    def device_class(self):
        """Return the device class of the sensor."""
        return self._device_class


class RTBBinarySensor(CoordinatorEntity, BinarySensorEntity):
    """Representation of an RTB binary sensor."""

    def __init__(self, coordinator, name, client_key, device_class):
        """Initialize the binary sensor."""
        super().__init__(coordinator)
        self.client_key = client_key
        self._device_class = device_class
        self.sensorname = name

    @property
    def name(self):
        """Return the name of the binary sensor."""
        #_LOGGER.info(f"sensor.py RTBBinarySensor (name) returning \"NBE {self.sensorname}\"")
        return f"NBE {self.sensorname}"

    @property
    def is_on(self):
        _LOGGER.info("is_on called")
        """Return the state of the binary sensor."""
        s = self.coordinator.rtbdata.get(self.client_key)
        _LOGGER.info(f"sensor.py RTBBinarySensor (is_on) value \"{s}\"")
        if "power_pct" in self.client_key:
            return s != "0"
        if "off_on_alarm"  in self.client_key:
            return s == "2"    
        return s == "0"

    @property
    def device_class(self):
        """Return the device class of the binary sensor."""
        return self._device_class

