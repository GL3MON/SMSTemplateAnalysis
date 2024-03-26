from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_file : Path
    raw_data_file : Path
    
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir : Path
    raw_data_file : Path
    transformed_data_file : Path
    tokenizer_name : str
    
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    transformed_data_file : Path
    model_ckpt : str
    learning_rate : float
    per_device_train_batch_size : int
    per_device_eval_batch_size : int
    num_train_epochs : int
    weight_decay : float
    save_strategy : str
    