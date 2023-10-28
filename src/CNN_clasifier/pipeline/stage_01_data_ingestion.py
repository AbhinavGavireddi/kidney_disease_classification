from CNN_clasifier.config.configuration import configurationManager
from CNN_clasifier.component.data_ingestion import DataIngestion
from CNN_clasifier import logger

STAGE_NAME = 'DATA_INGESTION_STAGE'

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = configurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()

    
if __name__ == '__main__':
    try:
        logger.info(f"starting {STAGE_NAME:^20}")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"completed {STAGE_NAME:^20}")
    except Exception as e:
        logger.exception(e)
        raise e

