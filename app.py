# -*- coding: utf-8 -*-
"""
Created on Sun May  2 15:44:34 2021

@author: Bruno.Mesquita
"""

from flask import Flask
from flask_restful import Api
from resources.controllers.balance import Balance
from resources.controllers.reset import Reset
from resources.controllers.event import Event

app = Flask(__name__)
api = Api(app)

api.add_resource(Balance, '/balance')
api.add_resource(Reset, '/reset')
api.add_resource(Event, '/event')

if __name__ == '__main__':
    app.run(debug=False)