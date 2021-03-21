# Constants for use in messages
# Can use constants or number in messages and set-level
DEBUG = False
DETAIL = False



def off():
    global DEBUG, DETAIL
    DEBUG = False
    DETAIL = False
    print("***************** DEBUG TURNED OFF **********************")

def on():
    global DEBUG, DETAIL
    DEBUG = True
    DETAIL = False
    print("****************** DEBUG TURNED ON **********************")

def show_detail():
    global DEBUG, DETAIL
    DEBUG = True
    DETAIL = True
    print("*************** DEBUG DETAILS TURNED ON *****************")


def msg(*arg):
    global DEBUG
    if DEBUG:
        print(*arg)

def detail(*arg):
    global DETAIL
    if DETAIL:
        print(*arg)

