from flask import Flask, render_template
import requests

app = Flask(__name__)
BASE_URL = 'http://127.0.0.1:5000'


@app.route('/')
def home():

    endpoint = '/grocery'
    url = BASE_URL + endpoint

    response = requests.get(url)

    groceries = response.json()

    return render_template('home.html', groceries=groceries)


@app.route('/add')
def add():

    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True, port=5001)
