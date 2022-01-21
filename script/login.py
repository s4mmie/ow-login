import pygetwindow as gw
from pynput.keyboard import Controller, Key
import random
import time
keyboard = Controller()
open_amount = 6

with open("email.txt") as f:
    email = f.read().splitlines()
with open("password.txt") as a:
    password = a.read().splitlines()
def type_d(string):
    for character in string:  # Loop over each character in the string
        keyboard.type(character)  # Type the character
        delay = random.randrange(0, 10)  # Generate a random number between 0 and 10
        delay = delay/5000
        time.sleep(delay)  # Sleep for the amount of seconds generated
def login_overwatch():
 overwatch = gw.getWindowsWithTitle('Overwatch')

 if(len(overwatch) > 0):
     x=0
     for x in range(0,open_amount):
         overwatch[x].minimize()
         overwatch[x].restore()
         overwatch[x].activate()

         type_d(email[x])
         time.sleep(.1)
         keyboard.press(Key.tab)
         time.sleep(.1)
         keyboard.release(Key.tab)
         time.sleep(.1)
         type_d(password[x])
         time.sleep(.1)
         keyboard.press(Key.enter)
         time.sleep(.05)
         keyboard.release(Key.enter)
         time.sleep(.1)

login_overwatch()
