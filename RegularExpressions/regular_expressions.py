#!/usr/bin/python

import configparser
import re

config = configparser.ConfigParser(interpolation=None)
config.read('settings/config.ini')


def check_value(value, regex):
    return 'VALID' if re.fullmatch(regex, value) else 'NOT valid'


print()
print('*****************************************************************')
print('******* Working With Regular Expressions Programmatically *******')
print('*****************************************************************')
print()

print('========== Phone Number Pattern Validation ===========')
phone_regex = config.get("PHONE_NUMBER", "REGEX")
print(f'Regular Expression: {phone_regex}\n')
phone_number = input('Please enter a phone number:\n')
print(f'Phone number: {phone_number} is {check_value(phone_number, phone_regex)}\n')

print('========== Email Address Pattern Validation ==========')
email_regex = config.get("EMAIL_ADDRESS", "REGEX")
print(f'Regular Expression: {email_regex}\n')
email_address = input('Please enter an Email address:\n')
print(f'Email address: {email_address} is {check_value(email_address, email_regex)}\n')

print('=============== URL Pattern Validation ===============')
url_regex = config.get("URL", "REGEX")
print(f'Regular Expression: {url_regex}\n')
url = input('Please enter a URL:\n')
print(f'The URL: {url} is {check_value(url, config.get("URL", "REGEX"))}\n')
