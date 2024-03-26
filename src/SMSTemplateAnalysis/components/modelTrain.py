from SMSTemplateAnalysis.entity import ModelTrainerConfig
from SMSTemplateAnalysis.logging import logger
from transformers import DataCollatorWithPadding
from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer
from transformers import TrainingArguments, Trainer
from datasets import load_metric
from datasets import load_from_disk
import torch
import os
import numpy as np

class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.model_ckpt)
        self.data_collator = DataCollatorWithPadding(tokenizer=self.tokenizer)
        
    def compute_metrics(logits, labels):
        load_accuracy = load_metric("accuracy")
        load_f1 = load_metric("f1")
        
        predictions = np.argmax(logits, axis=-1)
        accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
        accuracy = load_accuracy.compute(predictions=predictions, references=labels)["accuracy"]
        
        f1 = load_f1.compute(predictions=predictions, references=labels)["f1"]
        return {"accuracy": accuracy, "f1": f1}
        
    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"Running the model is {device}")
        logger.info(f"Loading model {self.config.model_ckpt}")
        model = AutoModelForSequenceClassification.from_pretrained(self.config.model_ckpt)
        
        training_args = TrainingArguments(
            output_dir=self.config.root_dir,
            learning_rate=self.config.learning_rate,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            per_device_eval_batch_size=self.config.per_device_eval_batch_size,
            num_train_epochs=self.config.num_train_epochs,
            weight_decay=self.config.weight_decay,
            save_strategy=self.config.save_strategy,
            push_to_hub=False,
        )
        
        
        dataset = load_from_disk(self.config.transformed_data_file)
        tokenized_train = dataset["train"]
        tokenized_eval = dataset["test"]
        
        trainer = Trainer(
            model= model,
            args= training_args,
            train_dataset= tokenized_train,
            eval_dataset= tokenized_eval,
            tokenizer= self.tokenizer,
            data_collator= self.data_collator,
            compute_metrics=self.compute_metrics,
        )
        
        logger.info("Initiating Training...")
        trainer.train()
        logger.info("Training done.")
        trainer.save_model(self.config.root_dir)
        logger.info("Save successfull.")