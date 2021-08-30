from server import find_country_info
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    try:
        return render_template('index.html')
    except:
        return redirect('/error')

@app.route('/error', methods=['GET'])
def error():
    return render_template('error.html')

@app.route('/api/<country>', methods=['GET', 'POST'])
def api(country):
    try:
        return find_country_info(str(country))
    except:
        return redirect('/error')