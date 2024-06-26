#!/usr/bin/python3

import requests
import bs4
import re
import os
import time
import colorama
from colorama import Fore
from colorama import Style

minerRegex = re.compile(r'coinhive.min.js|wpupdates.github.io/ping|cryptonight.asm.js|coin-hive.com|jsecoin.com|cryptoloot.pro|webassembly.stream|ppoi.org|xmrstudio|webmine.pro|miner.start|allfontshere.press|upgraderservices.cf|vuuwd.com')

possibleMinerfiles = re.compile('upgraderservices.cf|vuuwd.com')

def header():
    print(f'\n{Fore.GREEN}==============================================={Style.RESET_ALL}\n')

def scan2():
    try:
        requests.get('http://' + line.strip(), verify=False, timeout=5)
    except requests.exceptions.SSLError or requests.exceptions.ConnectionError or requests.exceptions.Timeout :
        pass


requests.packages.urllib3.disable_warnings()

#print('Do you want to scan a single site? [y/n]')
choice = input('Do you want to scan a single site? [y/n]')
if choice == "y" or choice == "Y":
    header()
    scansite = input("Enter the site to scan\n")

    try:
        scansite2 = requests.get('http://' + scansite)

        scansite2.raise_for_status()

        scansite3 = bs4.BeautifulSoup(scansite2.text, "html.parser")

        final = scansite3.find("script", text=minerRegex)

        print(final)
        header()
    except:
        print('Could not connect')

else:
#    print('multisite scanning not yet supported')
    multiscan = input("Provide a file containing the list of sites you want scanned: ")    
    
    assert os.path.exists(multiscan), "I did not find the file at, "+str(multiscan)
    scanfile = open(multiscan,'r+')

    header()
    for line in scanfile:
        print('Scanning:' + line)
        try:
            multiscan2 = requests.get('http://' + line.strip(), verify=False, timeout=5)
            multiscan2.raise_for_status()
            multiscan3 = bs4.BeautifulSoup(multiscan2.text, "html.parser")
            multifinal = multiscan3.find("script", text=minerRegex)
#            if len(str(multifinal) > 16):
#                print('  ==MINER FOUND==  ')
#                print(multifinal)
#                header()
#            else:
            print(Fore.RED)
            print(multifinal)
            print(Style.RESET_ALL)
            header()
        except: 
            pass
            print('Connection issues')
            header()

    scanfile.close()