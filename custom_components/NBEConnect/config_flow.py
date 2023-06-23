import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

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

        # Load the labels from strings.json
        strings = await self.hass.async_add_executor_job(
            self.hass.config.path, "strings.json"
        )

      
        # Extract the title and fields from the strings
        title = strings.get("title")
        fields = strings.get("config", {}).get("fields", {})

        # Create the data schema with labels
        data_schema = vol.Schema({
            vol.Required("serial", description={"label": fields.get("serial", {}).get("label")}): str,
            vol.Required("password", description={"label": fields.get("password", {}).get("label")}): str,
            vol.Optional("ip_address", description={"label": fields.get("ip_address", {}).get("label")}): str,
        })

        # Show the configuration form to the user with title and labels
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            description_placeholders={"title": title},
            errors=errors
        )