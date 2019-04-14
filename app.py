from flask import Flask
from flask import request
from flask import render_template
from search import Search
from db import DataBase

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def search():
    string = request.form['text']
    results = Search('money', DataBase)
    return render_template('search.html', links=results)


if __name__ == '__main__':
    app.run()
