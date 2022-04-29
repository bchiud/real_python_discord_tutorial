import collections
import os

import yaml


class Settings(dict):
    def __init__(self, value=None):
        if value:
            super().__init__(value)
        else:
            with open(
                os.path.join(os.path.dirname(__file__), "settings.yaml")
            ) as fo:
                super().__init__(yaml.full_load(fo))


settings = Settings()
