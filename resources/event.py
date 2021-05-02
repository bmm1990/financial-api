# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:47:21 2021

@author: Bruno.Mesquita
"""

from flask_restful import Resource, request
from resources.services.account_services import execute_deposit

class Event(Resource):
    def post(self):
        rcv_json = request.get_json()
        if rcv_json["type"] == "deposit":
            deposit = execute_deposit(rcv_json["destination"], rcv_json["amount"])
        return {"destination": deposit}, 201