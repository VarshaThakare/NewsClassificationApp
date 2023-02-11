# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request, render_template
from src.preprocess import clean_text
import pickle


# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello world"
		return jsonify({'data': data})

        
        


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/varsha1', methods = ['GET'])
def disp1():

	return "<h1> Varsha </h1>"
    

def load_model(path):
        lr_file = open(path, mode ='rb')
        lr = pickle.load(lr_file)
        return lr

def pred(input_text,model):
        input_text = clean_text(input_text)
        return model.predict([input_text])
        
@app.route('/varsha2', methods = ['GET','POST'])

def disp2():

    if (request.method == 'POST'):
    
        input_text = request.form['input_text']
    
        
        pred_text = pred(input_text,model)
    
        return f"<h1> The prediction is {pred_text} </h1>"
  
    return render_template("index.html")
    



# driver function
if __name__ == '__main__':

    model = load_model('models/news_classification_app_lr.pkl')
    app.run(host='0.0.0.0', port=5050, debug = False)
