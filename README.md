# SMS Template Analyser using fine-tunned BERT Model
This fine-tunned model analyses the received text message as spam or not. For this specific NLP task we use a simple Encoder Only pretrained Model developed by Google, named BERT. It performs exceptionally well in NLP task because of its bi-directional nature.
We use huggingface and pytorch library to load and fine tune the model.
## How to use
After cloning the current Repository. Run these commands to setup the environment.
```
python -r requirements.txt
python main.py
```
After the setup completes, run the app.py to check the inference of the pretrained model.
```
python app.py
```
