# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:47:21 2021

@author: Bruno.Mesquita
"""

from flask_restful import Resource, request
from resources.services.account_services import execute_deposit
from resources.services.account_services import execute_withdraw
from resources.services.account_services import execute_transfer

class Event(Resource):
    def post(self):
        rcv_json = request.get_json()
        if rcv_json["type"] == "deposit":
            deposit = execute_deposit(rcv_json["destination"], rcv_json["amount"])
            return {"destination": deposit}, 201
        elif rcv_json["type"] == "withdraw":
            withdraw = execute_withdraw(rcv_json["origin"], rcv_json["amount"])
            if withdraw == 0:
                return withdraw, 404
            else:
                return withdraw, 201
        elif rcv_json["type"] == "transfer":
            transfer = execute_transfer(rcv_json["origin"], rcv_json["amount"], rcv_json["destination"])
            if transfer == 0:
                return transfer, 404
            else:
                return transfer, 201
        else:
            return "Invalid request", 406

                