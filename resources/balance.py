# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:41:38 2021

@author: Bruno.Mesquita
"""

from flask_restful import Resource, request
from resources.services.account_services import get_account_balance


class Balance(Resource):
    def get(self):
        account_id = request.args.get('account_id')
        balance = get_account_balance(account_id)
        if balance == 0:
            return balance, 404
        else:
            return balance, 201