import json
from pathlib import Path

import yaml


def read_data(path):
    with open(path, encoding="utf-8") as file:
        expansion = Path(path).suffix
        match expansion:
            case ".json":
                return json.load(file)
            case ".yaml" | ".yml":
                return yaml.safe_load(file)