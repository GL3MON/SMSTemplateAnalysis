from SMSTemplateAnalysis.pipeline import prediction
from SMSTemplateAnalysis.pipeline.prediction import PredictionPipeline

prediction = PredictionPipeline()
while(1):
    print(prediction.predict(input("Enter the message: \n")))