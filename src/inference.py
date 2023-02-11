from preprocess import clean_text
import pickle

def load_model(path):
    lr_file = open(path, mode ='rb')
    lr = pickle.load(lr_file)
    return lr

def pred(input_text,model):
    input_text = clean_text(input_text)
    return model.predict([input_text])

raw_text = input("enter the text: ")
model = load_model('../models/news_classification_app_lr.pkl')
result = pred(raw_text,model)

print(result)
    