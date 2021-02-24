import requests, json
from bs4 import BeautifulSoup as soup 
import os,time

import colorama
from colorama import init,Back,Fore
init()
try:
	os.system("cls")
except:
	os.system("clear")


banner=""" _____          _ _               _____                           
|_   _|        | (_)             /  ___|                          
  | | _ __   __| |_  __ _  ___   \ `--.  ___ _ __ __ _ _ __   ___ 
  | || '_ \ / _` | |/ _` |/ _ \   `--. \/ __| '__/ _` | '_ \ / _ \
 _| || | | | (_| | | (_| | (_) | /\__/ / (__| | | (_| | |_) |  __/
 \___/_| |_|\__,_|_|\__, |\___/  \____/ \___|_|  \__,_| .__/ \___|
                     __/ |                            | |         
                    |___/                             |_|                               
 """


a = open("./proxies/https.txt","r+")
b = open("./proxies/socks4.txt","r+")
c = open("./proxies/socks5.txt","r+")

class scrapy():
	
	def get(self):
		url = ("http://proxy-daily.com/")
		req = requests.get(url)
		try:
			k = soup(req.text,"lxml")
		except:
			k = soup(req.text,"html")
		proxies = k.find_all("div",{"class":"centeredProxyList freeProxyStyle"})
		self.write(proxies)	
	def write(self,proxies):
		print(proxies[0],file=a)
		print(proxies[1],file=b)
		print(proxies[2],file=c)
		
if __name__ == '__main__':
	print(Fore.RED+banner)
	print(Fore.RED+Back.YELLOW)
	print("wait...")
	time.sleep(2)
	scrapy().get()


print("EXTRACCION COMPLETA:)")