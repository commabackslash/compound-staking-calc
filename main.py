# Written by commabackslash

from mimetypes import init
from time import time
import requests
import urllib.request

# this doesnt work yet but soon maybe
#api_key = ""
#api_url = "https://api.nomics.com/v1/currencies/ticker?key=" + api_key + "&ids=ZIL&interval=1d,30d&convert=USD&platform-currency=ETH&per-page=100&page=1"

time_passed =  0
i = 0

initial_investment = input("Initial staked amount: ")
yearly_return_perctange = input("Yearly return %: ")
time_period = input("How many months will you stake?: ")

months = int(time_period)

daily_return_percentage = int(yearly_return_perctange) / 365 / 100
daily_stake_reward = float(daily_return_percentage) * float(initial_investment)

print("__________________________")

for i in range(months):
    
    for i in range(30):

        initial_investment = float(initial_investment) * float(daily_return_percentage) + float(initial_investment)

    time_passed =  time_passed + 1
    print ("Month " + str(time_passed) + ":  " + str(initial_investment))

