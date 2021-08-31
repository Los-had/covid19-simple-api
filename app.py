from server import find_country_info
from flask import Flask, render_template, redirect, request, url_for
import os

app = Flask(__name__)
# app secret key
KEY = os.environ.get('KEY')
app.config['SECRET_KEY'] = KEY

@app.route('/', methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except:
        return redirect('/error')

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/api/<country>', methods=['GET'])
def api(country):
    try:
        return find_country_info(str(country).replace(' ', '-').capitalize())
    except:
        return redirect('/error')

if __name__ == '__main__':
    app.run(debug=True) # runs the app with debug mode on