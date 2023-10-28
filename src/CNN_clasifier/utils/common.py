import os
import yaml
import json
import joblib
import base64

from CNN_clasifier import logger
from box import exceptions, ConfigBox
from box.exceptions import BoxValueError

from ensure import ensure_annotations
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(yaml_path: Path) -> ConfigBox:
    try:
        with open(yaml_path, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"{os.path.split(yaml_path)[-1]} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(directories_paths: list, verbose:bool=True):
    for path in directories_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at : {path}")


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"json file saved at {path}")


def decode_image(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, "w") as f:
        f.write(imgdata)
    logger.info(f"image decoded")


def encode_image_into_base64(cropped_image_path):
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read())
