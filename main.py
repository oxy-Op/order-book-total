import requests
from time import sleep
from json import load
from datetime import datetime
from os import system
import sys
from colorama import Fore, init, Style

init(autoreset=True)

data = load(open('config.json'))
r_url = data['url']
limit = data['limit']
currency = data['currency']
delay = data['delay']
result = {}


class GetOrderBook:
    def __init__(self) -> None:
        self.url = r_url + "?limit=" + str(limit) + "&symbol=" + currency
        self.totalBids = 0
        self.totalAsks = 0
        self.currency = currency
        self.limit = limit

    def getData(self):
        try:
            req = requests.get(self.url)
            print("Quantity | Currency: {} | Limit: {} | Datetime: {} ".format(
                self.currency, self.limit, datetime.now()))
            result.update(req.json())

        except KeyError:
            return "KeyError: Please confirm your data"

    def bids(self):
        for i in result['bids']:
            self.totalBids += float(i[1])
            print("Bids: ", i[1])
        print("Total Bids: ", self.totalBids, "\n")

    def asks(self):
        for i in result['asks']:
            print(self.totalAsks)
            self.totalAsks += float(i[1])
            print(i)
            print(self.totalAsks)
            print("Asks: ", i[1])
        print("Total Asks: ", self.totalAsks, "\n")

    def animate(self, r):
        for i in range(1, r + 1):
            sleep(i)
            print(f"Clearing in {i} second")

    def persistence(self):
        x = 0
        y = 0
        f = open("values.txt", 'a').write("------------------ \n")
        while True:
            self.totalAsks = 0
            self.totalBids = 0
            file = open("logs.txt", "a")
            c = open("values.txt", "a")
            self.getData()
            file.write(str("Quantity | Currency: {} | Limit: {} | Datetime: {} \n".format(
                self.currency, self.limit, datetime.now())))
            for i in result['asks']:
                self.totalAsks += float(i[1])
                y += float(i[1])
                print(Fore.RED+Style.BRIGHT+"Sell: " + str(i[1]))
                file.write(f"Sell  : {str(i[1])} \n")
            print(Style.BRIGHT + Fore.MAGENTA +
                  "Total Sell: " + str(self.totalAsks), "\n")
            file.write("Total Sell: " + str(self.totalAsks) + "\n")
            for i in result['bids']:
                self.totalBids += float(i[1])
                x += float(i[1])
                print(Fore.GREEN + "Buy: " + str(i[1]))
                file.write(f"Buy : {str(i[1])} \n")
            print(Style.BRIGHT + Fore.MAGENTA + "Total Buy: " +
                  str(self.totalBids), "\n")
            file.write("Total Buy: " + str(self.totalBids) + "\n")
            print("\n \nTotal Buy {} | Total Sell {} \n \n".format(
                self.totalBids, self.totalAsks))
            c.write(f"Total Sell {y} | Total Buy {x} \n")
            self.animate(delay)
            system('cls')
            file.close()
            c.close()


GetOrderBook().persistence()
