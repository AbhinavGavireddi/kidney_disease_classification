from src.CNN_clasifier import logger
from src.CNN_clasifier.pipeline.stage_01_data_ingestion import (
    DataIngestionTrainingPipeline,
)
from src.CNN_clasifier.pipeline.stage_02_prepare_base_model import (
    PrepareBaseModelPipeline,
)

logger.info("Welcome to Kidney disease prediction App")


# STAGE_NAME = "Data Ingestion Stage"
# try:
#     logger.info(f"starting {STAGE_NAME:^30}")
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info(f"completed {STAGE_NAME:^30}")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "Prepare Base Model"

try:
    logger.info(f"starting {STAGE_NAME:^20}")
    obj = PrepareBaseModelPipeline()
    obj.main()
    logger.info(f"completed {STAGE_NAME:^20}")
except Exception as e:
    logger.exception(e)
    raise e
