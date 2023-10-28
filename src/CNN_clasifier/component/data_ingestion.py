import os
import zipfile
import gdown
from CNN_clasifier.entity.config_entity import DataIngestionConfig
from CNN_clasifier.utils.common import logger
class DataIngestion:
    def __init__(self,config :DataIngestionConfig) -> None:
        self.config = config
    
    def download_data(self):
        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs(self.config.root_dir,exist_ok=True)
            logger.info(f"Downloading Data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,zip_download_dir)
            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file) as zip_ref:
            zip_ref.extractall(unzip_path)