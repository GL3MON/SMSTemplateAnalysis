from SMSTemplateAnalysis.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from SMSTemplateAnalysis.pipeline.data_transformation_pipeline import DataTransformationPipeline
from SMSTemplateAnalysis.pipeline.model_train_pipeline import ModelTrainPipeline
from SMSTemplateAnalysis.pipeline.prediction import PredictionPipeline
from SMSTemplateAnalysis.logging import logger

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Train"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_train_pipeline = ModelTrainPipeline()
    model_train_pipeline.main()
except Exception as e:
    logger.exception(e)
    raise e
    
