import voluptuous as vol

DOMAIN = "nbeconnect"
DATA_SCHEMA = vol.Schema(
                {
                    vol.Required("serial"): str,
                    vol.Required("password"): str,
                    vol.Optional("ip_address"): str,
                })
PLATFORMS = ['sensor', 'button']