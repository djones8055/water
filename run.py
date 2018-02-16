#!/usr/bin/python3

import os
import setup


def getinput():

    getmenu = input('Press 1 to make one or 2 to quit. ')

    while True:
        try:
            if int(getmenu) != 1 and int(getmenu) != 2:
                print()
                print('Invalid input.')
                getmenu = input('Press 1 to make one or 2 to quit. ')
                print()

            else:
                break

        except ValueError:
            print()
            print('Invalid input.')
            getmenu = input('Press 1 to make one or 2 to quit. ')
            print()

    return int(getmenu)


if not os.path.isfile('config.txt'):
    print()
    print('No config fle found')
    print()

    firsttimemenu = getinput()

    if firsttimemenu == 1:
        # setup
        setup.getaddress()

    elif firsttimemenu == 2:
        print('Quitting.')
        exit()
