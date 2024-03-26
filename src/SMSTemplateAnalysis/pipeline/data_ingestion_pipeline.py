from SMSTemplateAnalysis.components.dataIngestion import DataIngestion
from SMSTemplateAnalysis.config.configuration import ConfigurationManager
from SMSTemplateAnalysis.logging import logger

class DataIngestionPipeline:
    
    def __init__(self) -> None:
        pass
    
    def main(self):
        logger.info("Data Ingestion Pipeline Started")
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.load_data()
        logger.info("Data Ingestion Pipeline Completed")
        
