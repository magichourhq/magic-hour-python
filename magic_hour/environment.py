import enum


class Environment(enum.Enum):
    """Pre-defined base URLs for the API"""

    ENVIRONMENT = "https://api.magichour.ai"
    MOCK_SERVER = "https://api.sideko.dev/v1/mock/magichour/magic-hour/0.9.5"
