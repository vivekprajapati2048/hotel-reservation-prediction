import os
import pandas as pd
from loguru import logger
from src.custom_exception import CustomException
import yaml

def read_yaml(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("File not found at the given path.")
        
        with open(file_path, "r") as yaml_file:
            config = yaml.safe_load(yaml_file)
            logger.info("Successfully read the YAML file.")
            return config

    except Exception as e:
        logger.exception("Error reading YAML file.")
        raise CustomException(f"Failed to read YAML file: {e}")
    

def load_data(path):
    try:
        logger.info("Loading data")
        return pd.read_csv(path)
    except Exception as e:
        logger.error(f"Error loading the data {e}")
        raise CustomException("Failed to load data",  str(e))
