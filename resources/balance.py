# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:41:38 2021

@author: Bruno.Mesquita
"""

from flask_restful import Resource, request

class Balance(Resource):
    def get(self):
        account_id = request.args.get('account_id')
        return account_id, 200