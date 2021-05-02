# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:44:34 2021

@author: Bruno.Mesquita
"""

from flask import Flask
from flask_restful import Api
from resources.helloworld import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)