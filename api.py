# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:44:34 2021

@author: Bruno.Mesquita
"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)