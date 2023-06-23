import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, DATA_SCHEMA

class NbertbConfigFlow(config_entries.ConfigFlow, domain = DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            # Validate the user input
            if not user_input.get("serial"):
                errors["base"] = "missing_serial"
            if not user_input.get("password"):
                errors["base"] = "missing_password"

            if not errors:
                # Configuration is valid, create the entry
                return self.async_create_entry(title="NBEConnect by SVANGGAARD", data=user_input)

        # Show the configuration form to the user
        return self.async_show_form(
            step_id="user",
            data_schema=DATA_SCHEMA,
            errors=errors
        )