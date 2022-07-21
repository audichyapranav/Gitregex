from multiprocessing.sharedctypes import Value
from optparse import Values
from unittest.loader import VALID_MODULE_NAME


lst = []
while True:
    commands = input("enter the operation:  ")
    list = commands.split()
    if commands == 'stop':
        break
    elif commands == 'push':
        lst.append(value[1])
    elif commands =='pop':
        index_of_value = lst.index(value[1])
        lst.pop(index_of_value)
    else:
        print('Invalid Commands')
        continue
        