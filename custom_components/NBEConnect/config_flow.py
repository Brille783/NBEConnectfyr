import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN
from homeassistant.helpers.selector import (
    TextSelector,
    TextSelectorConfig,
    TextSelectorType,
)


class NbeConnectConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
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
                return self.async_create_entry(title="NBEConnect by svj", data=user_input)
        
        
        STEP_USER_DATA_SCHEMA = vol.Schema(
            {
                vol.Required("serial"): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.TEXT, autocomplete="serial")
                ),
                vol.Required("password"): TextSelector(
                    TextSelectorConfig(
                        type=TextSelectorType.PASSWORD, autocomplete="password"
                    )
                ),
                vol.Optional("ip_address"): TextSelector(
                    TextSelectorConfig(type=TextSelectorType.TEXT, autocomplete="Fixed ip")
                )
            })

        # Show the configuration form to the user with title and labels
        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors
        )