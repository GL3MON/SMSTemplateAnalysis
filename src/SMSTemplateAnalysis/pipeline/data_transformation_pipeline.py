from SMSTemplateAnalysis.components.dataTransformation import DataTransformation
from SMSTemplateAnalysis.config.configuration import ConfigurationManager
from SMSTemplateAnalysis.logging import logger

class DataTransformationPipeline:
    
    def __init__(self) -> None:
        pass
    
    def main(self):
        logger.info("Data Transformation Pipeline Started")
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        logger.info("Transforming data")
        data_transformation.transform_data()
        logger.info("Data Transformation Pipeline Completed")

