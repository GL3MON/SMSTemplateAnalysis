from SMSTemplateAnalysis.components.modelTrain import ModelTrainer
from SMSTemplateAnalysis.config.configuration import ConfigurationManager
from SMSTemplateAnalysis.logging import logger

class ModelTrainPipeline:
    
    def __init__(self) -> None:
        pass
    
    def main(self):
        logger.info("Training Pipeline is started")
        config = ConfigurationManager()
        model_train_config = config.get_model_train_config()
        model_train = ModelTrainer(config=model_train_config)
        model_train.train()
        logger.info("Training Pipeline ended.")
        