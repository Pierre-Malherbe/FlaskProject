#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello ! Bienvenue sur le projet AWS"

if __name__ == '__main__':
    app.run(debug=True)
