from flask import Flask, render_template, request
import tensorflow as tf
# Import your models
from model.english_to_shakespeare_translator import  Translator_Model
#from mnist_predictor import MNIST_predictor
physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)
app = Flask(__name__)

# Instantiate your models
model =  Translator_Model()
#mnist = MNIST_predictor()


# Base endpoint to perform prediction.
@app.route('/', methods=['POST'])
def make_prediction():
    #if request.form['predictor'] == 'translate':
    #    prediction = mnist.predict(request)
    #    return render_template('index.html', prediction=prediction, generated_text=None, tab_to_show='mnist')

    if request.form['predictor'] == 'gpt2':
        print(len(request.form['starting_tokens']))
        text = request.form['starting_tokens']
        generated_text = model.translate(text)
        return render_template('index.html', prediction=None, generated_text=generated_text, tab_to_show='gpt2')


@app.route('/', methods=['GET'])
def load():
    return render_template('index.html', prediction=None, generated_text=None, tab_to_show='mnist')



@app.route('/predict/text', methods=['POST'])
def make_text_prediction():
    prediction = model.translate(request.form['starting_tokens'])
    return prediction

if __name__ == '__main__':
    app.run(debug=True)
