#More Information from get_accurate_gains.py
#Updated by Christopher Snell, 14 September 2019

import robin_stocks as r

'''
Robinhood includes dividends as part of your net gain. This script removes
dividends from net gain to figure out how much your stocks/options have paid
off.

Note: load_portfolio_profile() contains some other useful breakdowns of equity.
Print profileData and see what other values you can play around with.

'''

#!!! Fill out username and password
username = ''
password = ''
#!!!

login = r.login(username,password)

profileData = r.load_portfolio_profile()
#print(profileData)
allTransactions = r.get_bank_transfers()

deposits = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'deposit') and (x['state'] == 'completed'))
withdrawals = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'withdraw') and (x['state'] == 'completed'))
money_invested = deposits - withdrawals

dividends = r.get_total_dividends()
percentDividend = dividends/money_invested*100

totalGainMinusDividends =float(profileData['extended_hours_equity'])-dividends-money_invested
extendedHours = float(profileData['extended_hours_equity'])
percentGain = totalGainMinusDividends/money_invested*100

totalEquity = float(profileData['extended_hours_equity'])

print("The total money invested is {}".format(money_invested))
print("Total Equity is {}".format(totalEquity))
print("Extended Hours is {}.".format(extendedHours))
print("Amount received in dividends: {}".format(dividends))
print("Money invested plus dividends: {}".format(money_invested + dividends))
print("The net worth has increased {:0.2}% due to dividends".format(percentDividend))
print("The net worth has increased {:0.3}% due to other gains".format(percentGain))

equation = (float(totalEquity) - float(money_invested))/money_invested * 100
print("The total net worth has increased {:0.3}%".format(equation))
