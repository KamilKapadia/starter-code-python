#!/usr/bin/python

import sys

print()
print('**************************************************************');
print('********** Working With User Input Programmatically **********');
print('**************************************************************');
print();

print('===== Input from Command Line Args =====')
if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        print(arg)
else:
    print('No command line args found')
print()

print('===== Input from prompts =====')
name = input('Please enter your name: ')
print(f'Hello {name}')
print()
