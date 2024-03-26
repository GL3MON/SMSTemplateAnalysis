from SMSTemplateAnalysis.constants import *
from SMSTemplateAnalysis.utils.common import read_yaml, create_directories
from SMSTemplateAnalysis.entity import (DataIngestionConfig, DataTransformationConfig,ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self, config_filepath = CONFIG_PATH):
        self.config = read_yaml(config_filepath)
        
        create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config  = self.config.data_ingestion
        
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            raw_data_file=config.raw_data_file,
        )
        
        return data_ingestion_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        
        config = self.config.data_transformation
        
        create_directories([config.root_dir])
        
        data_transformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            raw_data_file=config.raw_data_file,
            transformed_data_file=config.transformed_data_file,
            tokenizer_name = config.tokenizer_name,
        )
            
        return data_transformation_config
    
    def get_model_train_config(self) -> ModelTrainerConfig:
        
        config = self.config.model_train
        
        create_directories([config.root_dir])
        
        model_train_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            transformed_data_file=config.transformed_data_file,
            model_ckpt=config.model_ckpt,
            learning_rate=config.learning_rate,
            per_device_train_batch_size=config.per_device_train_batch_size,
            per_device_eval_batch_size=config.per_device_eval_batch_size,
            num_train_epochs= config.num_train_epochs,
            weight_decay= config.weight_decay,
            save_strategy= config.save_stratergy
        )
        
        return model_train_config
        