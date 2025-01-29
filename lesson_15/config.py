import pathlib
import yaml


BASE_DIR = pathlib.Path(__file__).parent  

config_path = BASE_DIR / "config.yml"


def get_config(path):
  with open(path, "r", encoding="utf-8") as f:
    return yaml.safe_load(f)


config = get_config(config_path)


DB_CONFIG = config["db"]

PORT = config["common"]["port"]
print(PORT, DB_CONFIG)
