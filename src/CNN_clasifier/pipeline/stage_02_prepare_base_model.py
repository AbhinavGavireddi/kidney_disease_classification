from CNN_clasifier.config.configuration import configurationManager
from CNN_clasifier.component.prepare_base_model import PreparebaseModel
from CNN_clasifier import logger

STAGE_NAME = 'MODEL_PREPARATION_STAGE'

class PrepareBaseModelPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = configurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PreparebaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

    
if __name__ == '__main__':
    try:
        logger.info(f"starting {STAGE_NAME:^20}")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f"completed {STAGE_NAME:^20}")
    except Exception as e:
        logger.exception(e)
        raise e



