#Updated by Christopher Snell
#Portfolio
# 15 September 2019

# Run command -- python3 showstocks.py > mystocks.txt
#
#
# Perform command -- cat mystocks.txt | grep -B 1 -A 6 "\Symbol:KO\n"
# This will show one line before and 6 lines after
# This will display the stock information appropriately

from pprint import pprint
  
import robin_stocks as r
import requests
import wget
import json
import stocks as s
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
                continue
        except:
                continue


        try:
                print("Name:" + str(jdata['simple_name']))
        except ValueError as f:
                continue
        except:
                continue
        print("Symbol:" + jdata['symbol'])
        print("Shares:" + counter['quantity'])
        bvalue = str(jdata['symbol'])
        try:
                cvalue = list(s.get_latest_price(bvalue))
        except ValueError as g:
                continue
        except: 
                continue

     
        if len(cvalue) != 0:
            print("Price:" + str(cvalue[0]))
            print("Average Cost:" + counter['average_buy_price'])       
            #bvalue = str(jdata['symbol'])
            #cvalue = s.get_latest_price(bvalue)
            #print("Price:" + str(cvalue))
	    #cvalue = str(get_quotes(bvalue))
            #print(cvalue)
	    #print(tSymbol)
	    #print(get_latest_price(jdata['symbol']))
	    #myprice = get_latest_price(jdata['symbol'])
	    #print("Average Cost:" + counter['average_buy_price'])
            print("Total Return:" + str(float(cvalue[0])*float(counter['quantity']) - float(counter['average_buy_price'])*float(counter['quantity']))) #Need active price of stock to calculate
            print("Equity:" + str(float(cvalue[0])*float(counter['quantity']))) #Need active price of stock to calculate
            print("\n")

