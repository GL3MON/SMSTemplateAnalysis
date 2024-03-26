from SMSTemplateAnalysis.logging import logger
from SMSTemplateAnalysis.entity import DataTransformationConfig
from SMSTemplateAnalysis.utils.common import get_size
from transformers import AutoTokenizer
from datasets import load_from_disk
import os
from pathlib import Path

class DataTransformation:
    def __init__(self, config : DataTransformationConfig) -> None:
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_to_features(self, example_batch) -> dict:
        return self.tokenizer(example_batch["sms"], truncation=True)
        
    
    def transform_data(self) -> None:
        if not os.path.getsize(self.config.root_dir):
            logger.info("Loading dataset from disk")
            raw_dataset = load_from_disk(self.config.raw_data_file)
            raw_dataset = raw_dataset['train']
            logger.info("Loaded successfully")
            logger.info("Spliting dataset into train and test sets")
            raw_dataset = raw_dataset.train_test_split(test_size=0.2)
            logger.info("Splitting completed successfully")
            dataset = raw_dataset.map(self.convert_to_features, batched=True)
            dataset.save_to_disk(self.config.transformed_data_file)
            
            
            
        