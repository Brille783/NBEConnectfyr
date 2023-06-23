from logging import getLogger

_LOGGER = getLogger(__name__)

class RTBData:
    def __init__(self, data: list = None):
        self.m_data = [] if data is None else data

    def set(self, data: list):
        if data is not None:
            self.m_data = data
        else:
            self.m_data = []

    def get(self, varname: str):
        for item in self.m_data:
            key, value = item.split('=')
            if varname in key:
                try:
                    _LOGGER.debug(f"RTBData {varname} is {value}")
                    return value
                except ValueError:
                    _LOGGER.error(f"Value for {varname} could not be converted to float. Actual value: {value}")
        return None