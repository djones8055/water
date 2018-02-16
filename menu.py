#!/usr/bin/python3

def strinput(strquestion,strtitle = 0, strlength = 0):

    if strtitle != 0:
        print(strtitle)

    answer = str(input(strquestion))

    # add a length checker using strlength to input
    # either minimum or exact number of chars

    return answer

def inputint(intquestion, inttitle =0, intrange = 0):

    if inttitle != 0:
        print()
        print(inttitle)
        print()

    intreturn = input(intquestion)

    while True:
        try:
            int(intreturn)

        except ValueError:
            print('Invalid input')
            intreturn = input(intquestion)

        else:
            break
    return intreturn

def formatmenu():
    return

def servemenu():
    return