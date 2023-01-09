#!/usr/bin/env python3

import requests
import re
import random
import time 

R  = '\033[31m' # red
G  = '\033[32m' # green

def extractSource(username):
    useragents = open('useragents.txt').read().splitlines()
  
    with open('websitelist.txt') as f:
        for site in f:
          site = site.strip()
          useragent = random.choice(useragents)
          headers = {
              "User-Agent": useragent
            }
          site = site + username
          r = requests.get(site, headers=headers)
          parseHTML(r, username, site)
                      
def parseHTML(request, username,site): 
  if request.status_code == 200:
    match = re.search(username, request.text)
    if match != "":
        print(G +"Account found on: " + site+ G)
        time.sleep(3)
    elif request.status_code != 200:
        print(R+"Account not found on: " + site + "[Status Code: " + str(request.status_code) +"]"+R)
        time.sleep(3)

def main():
  
  userName = input("Enter a username : ")
  
  extractSource(userName)

if __name__ == "__main__":
    main()