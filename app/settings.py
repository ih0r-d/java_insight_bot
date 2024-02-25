import json
from pathlib import Path
from typing import Dict, Any

CONFIG_FILE = 'config.json'


def __get_root_path() -> Path:
    return Path(__file__).parent.parent.joinpath(CONFIG_FILE)


def _read_config() -> Dict[str, Any]:
    root_path = __get_root_path()
    with open(root_path) as f:
        return json.load(f)


class Bot:
    def __init__(self, data):
        self.token = data['token']


def get_bot_config() -> Bot:
    app_config = _read_config()
    return Bot(app_config['bot'])
