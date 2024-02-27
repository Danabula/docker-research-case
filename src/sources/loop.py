from os import environ
from time import time, sleep
from typing import Any
import signal


# global state
running = True


# python images blijken sigterm niet te handelen
# (dat wordt verstuurd bij ctrl+c in een terminal emulator en docker stop)
# registreer sigterm handler en stop de loop
def sigterm_handler(signum: int, frame: Any):
    global running
    print("got sigterm")
    running = False
signal.signal(signal.SIGTERM, sigterm_handler)


# print bericht of tijd elke seconde
while running:
    sleep(1)
    print(environ.get("MESSAGE", "time " + str(time())))
