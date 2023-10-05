"""
This program is used for MGTC28 In-class Assignment 4.
timer.py is a simple Python script that facilitates the Nerves of Steel game.
Program will inform players of when to stand, and set a random timer between 5-25 seconds.
Upon timer expiry, program will display text informing user time is up.
timer.py uses the time library to help keep track of time.
timer.py uses the random library to generate a random number within range.
"""


# This program is timer that counts down


import time # The time library has a sleep function that will pause the script for a specifized amount of time

import random # The random library allows us to generate a random number between 5-25 seconds.

print("Players stand") # Program to display text informing players to stand

# ask user to enter desired countdown time
set_time = random.randint(6, 24) # Random time between 5-25 seconds, therefore any number from 6-24.

time.sleep(set_time) # Program sleeps duration of random time chosen


print("Time Up. Last to sit down wins.") # Program to display text informing players time is up
