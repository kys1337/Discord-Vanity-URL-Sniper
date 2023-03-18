from datetime import datetime
from threading import Thread
from colorama import Fore
import requests
import psutil
import json
import os
from pymongo import MongoClient
from pystyle import *
import os
import subprocess
import requests
from colorama import *
import time
import socket
import uuid
import getpass



def start():
    intro = """

                ██░ ██  ▄▄▄       ██▀███  ▓█████  ███▄ ▄███▓
                ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒
                ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ▓██    ▓██░
                ░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ 
                ░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░▒████▒▒██▒   ░██▒
                ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░
                ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░░  ░      ░
                ░  ░░ ░  ░   ▒     ░░   ░    ░   ░      ░   
                ░  ░  ░      ░  ░   ░        ░  ░       ░   
                                                            
                                 sys | mxra
  

> Press Enter                                 
    """

    
    Anime.Fade(Center.Center(intro), Colors.black_to_red, Colorate.Vertical, interval=0.035, enter=True)
    

    print(f"""{Fore.LIGHTRED_EX}


                                      ██░ ██  ▄▄▄       ██▀███  ▓█████  ███▄ ▄███▓
                                      ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▓█   ▀ ▓██▒▀█▀ ██▒
                                      ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒███   ▓██    ▓██░
                                      ░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄ ▒██    ▒██ 
                                      ░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒░▒████▒▒██▒   ░██▒
                                      ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░░ ▒░   ░  ░
                                      ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░░  ░      ░
                                      ░  ░░ ░  ░   ▒     ░░   ░    ░   ░      ░   
                                      ░  ░  ░      ░  ░   ░        ░  ░       ░   
                                                                                  
                                                      sys | mxra                                            
                                    
    """)

time.sleep(1)

dt = datetime.now().strftime('[%H:%M:%S]')
print(f'{Fore.LIGHTCYAN_EX}{dt} {Fore.LIGHTGREEN_EX}')

def change_vanity():
   payload = {"code": vanity_url}
   response = requests.patch(f"https://discord.com/api/v10/guilds/{guild_id}/vanity-url", headers=headers, json=payload)
   if response.status_code == 200:
      print(f"{Fore.LIGHTGREEN_EX}URL is succesfully changed. discord.gg/{vanity_url}")
      data = {"content" : f"discord.gg/{vanity_url} URL succesfully changed! ", "username" : "0007"}
      requests.post(webhook, json=data)
   else:
      print(f"{Fore.LIGHTRED_EX}Error Code : {response.status_code}")

def check_vanity():
   response = requests.get(f"https://discord.com/api/v9/invites/{vanity_url}?with_counts=true&with_expiration=true", headers=headers)
   if response.status_code == 404:
      change_vanity()
      exit()
   else:
      print(f'{Fore.LIGHTRED_EX}[vanity] Trying againg...{Fore.RESET}')

start()

token = input(f'{Fore.LIGHTCYAN_EX}Token: {Fore.RESET}> ')
webhook = input(f'{Fore.LIGHTCYAN_EX}Webhook: {Fore.RESET}> ')
vanity_url = input(f'{Fore.LIGHTCYAN_EX}Vanity URL: {Fore.RESET}> ')
guild_id = input(f'{Fore.LIGHTCYAN_EX}Vanity Server ID: {Fore.RESET}> ')
headers = {"authorization": token,
               "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

data = {
    "content": token
}

while True:
   check_vanity()
