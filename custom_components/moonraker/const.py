"""Constants for Moonraker."""
from homeassistant.const import Platform
from enum import Enum

# Base component constants
DOMAIN = "moonraker"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.4.0"
MANIFACTURER = "@marcolivierarsenault"

# Platforms
PLATFORMS = [Platform.SENSOR, Platform.CAMERA]

CONF_API_KEY = "api_key"
CONF_URL = "url"
CONF_PORT = "port"

# API dict keys
HOSTNAME = "hostname"
OBJ = "objects"


class METHOD(Enum):
    """API methods."""

    SERVER_FILES_METADATA = "server.files.metadata"
    SERVER_WEBCAMS_LIST = "server.webcams.list"
    PRINTER_INFO = "printer.info"
    PRINTER_OBJECTS_LIST = "printer.objects.list"
    PRINTER_OBJECTS_QUERY = "printer.objects.query"

    def __str__(self):
        """Return the method name."""
        return self.value
