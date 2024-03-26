import os
from SMSTemplateAnalysis.logging import logger
from pathlib import Path
from datasets import load_dataset
from SMSTemplateAnalysis.entity import DataIngestionConfig
from SMSTemplateAnalysis.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def load_data(self):
        if not os.path.getsize(self.config.local_data_file):
            logger.info("Loading dataset from HuggingFace")
            raw_dataset = load_dataset(self.config.source_url)
            logger.info(f"Saving dataset to {self.config.local_data_file}")
            raw_dataset.save_to_disk(self.config.raw_data_file)
        else:
            logger.info(f"File already exists at {self.config.local_data_file} of size {get_size(Path(self.config.local_data_file))}. Skipping download.")