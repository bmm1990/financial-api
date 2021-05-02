# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:06:58 2021

@author: Bruno.Mesquita
"""

accounts = []

def get_account_index(account_id):
    index = next((index for (index, d) in enumerate(accounts) if d["id"] == account_id), None)
    return index

def check_if_account_exists(account_id):
   index = get_account_index(account_id)
   return bool(index is not None)

def create_new_account(account_id, account_balance):
    new_account = {"id":account_id,"balance":account_balance}
    accounts.append(new_account)

def get_account_full_info(account_id):
   index = get_account_index(account_id)
   return accounts[index]

def add_amount_existing_account(account_id, amount):
   index = get_account_index(account_id)
   accounts[index]["balance"] = accounts[index]["balance"] + amount

def execute_deposit(account_id, account_balance):
    existing_account = check_if_account_exists(account_id)
    if existing_account:
        add_amount_existing_account(account_id, account_balance)
    else:
        create_new_account(account_id, account_balance)    
    return get_account_full_info(account_id)

def get_account_balance(account_id):
    existing_account = check_if_account_exists(account_id)
    if existing_account:
        index = get_account_index(account_id)
        return accounts[index]["balance"]
    else:
        return 0

