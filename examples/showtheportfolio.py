#Updated by Christopher Snell
#Portfolio
# 15 September 2019

from pprint import pprint
  
import robin_stocks as r
import requests
import wget
import json

'''
Robinhood portfolio script

'''

#!!! Fill out username and password
username = ''
password = ''
#!!!

login = r.login(username,password)

mypos = r.get_current_positions()


for counter in mypos:
        mystring = counter['instrument']
        myr = requests.get(mystring)
        try:
                jdata = (json.loads(myr.content))
        except ValueError as e:
                #print(" ")
                break

        try:
                print("Name:" + str(jdata['simple_name']))
        except ValueError as f:
                break
        print("Symbol:" + jdata['symbol'])
        print("Shares:" + counter['quantity'])
        print("Price: nil") #Need active price of stock to update
        print("Average Cost:" + counter['average_buy_price'])
        print("Total Return: nil") #Need active price of stock to calculate
        print("Equity: nil") #Need active price of stock to calculate
        print("\n")
