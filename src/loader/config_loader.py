import json
from pathlib import Path

HOME = str(Path.home())


def load_config(config_path="", encoding='utf-8'):

    if not config_path:
        config_path = "./config.json"
        
    config_path = config_path.replace('~', HOME)

    with open(config_path, encoding=encoding) as f:
        config = json.load(f)

    config['takeout-path'] = config['takeout-path'].replace('~', HOME)

    return config
