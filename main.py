from src.CNN_clasifier import logger
from src.CNN_clasifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)

logger.info("Welcome to Kidney disease prediction App")


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"starting {STAGE_NAME:^30}")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"completed {STAGE_NAME:^30}")
except Exception as e:
    logger.exception(e)
    raise e
