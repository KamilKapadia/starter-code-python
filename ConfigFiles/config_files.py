#!/usr/bin/python

import configparser

print()
print('**************************************************************')
print('********* Working With Config Files Programmatically *********')
print('**************************************************************')
print()

print('===== Properties from: config.ini =====')
config = configparser.ConfigParser()
config.read('settings/config.ini')

print(f'USER USERNAME  =  {config.get("USER", "USERNAME")}')
print(f'WEB URL        =  {config.get("WEB", "URL")}')
print(f'WEB PORT       =  {config.get("WEB", "PORT")}')
print()
