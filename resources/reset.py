# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:47:30 2021

@author: Bruno.Mesquita
"""

from flask_restful import Resource
from resources.services.account_services import execute_reset

class Reset(Resource):
    def post(self):
        execute_reset()
        return "OK", 200