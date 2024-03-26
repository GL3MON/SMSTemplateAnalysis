from SMSTemplateAnalysis.config.configuration import ConfigurationManager
from SMSTemplateAnalysis.logging import logger
from pathlib import Path
from transformers import pipeline

class PredictionPipeline:
    def __init__(self) -> None:
        logger.info("Starting Prediction Pipeline...")
        self.config = ConfigurationManager().get_model_train_config()
        
    def predict(self, text):
        prompt = []
        prediction_pipeline = pipeline("text-classification", model=Path(self.config.root_dir))
        prompt.append(text)        
        if prediction_pipeline(prompt)[0]["label"] == "LABEL_0":
            return "This is not a spam."
        else:
            return "This is a spam"
            
            
        
