#!/usr/bin/python3
import menu

""" set up config file"""


def buildconfig():
    return

def getaddress():

    
    streetnumber = menu.inputint('What is the street number? ', 'Gathering address information.')
    streetname = menu.strinput('What is the street name? ')
    cityname = menu.strinput('What city? ')
    statename = menu.strinput('What state? ')
    zipcode = menu.inputint('Zip code? ')

    # for testing, remove later
    print()
    print(streetnumber, streetname)
    print(cityname, statename, zipcode)
    return
