import os
from termcolor import cprint

def getprivs():
    user = os.getenv("SUDO_USER")
    if user is None:
        return "user"
    else:
        return "admin"
