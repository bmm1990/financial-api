# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:44:34 2021

@author: Bruno.Mesquita
"""

from flask import Flask
from flask_restful import Api
from resources.helloworld import HelloWorld
from resources.balance import Balance
#from resources.reset import Reset
from resources.event import Event

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/')
api.add_resource(Balance, '/balance')
#api.add_resource(Reset, '/reset')
api.add_resource(Event, '/event')

if __name__ == '__main__':
    app.run(debug=True)