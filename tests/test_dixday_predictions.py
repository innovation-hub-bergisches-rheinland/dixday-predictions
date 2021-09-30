import csv
import yaml

from dixday_predictions import __version__
from dixday_predictions.eventhandler.EventHandler import EventHandler


def _read_config(config_path) -> dict:
    with open(config_path, "r") as ymlfile:
        config = yaml.safe_load(ymlfile)
    return config


def test_version():
    assert __version__ == '0.1.5'
