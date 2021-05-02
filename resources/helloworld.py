# -*- coding: utf-8 -*-
"""
Created on Sun May  2 16:12:28 2021

@author: Bruno.Mesquita
"""

from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}