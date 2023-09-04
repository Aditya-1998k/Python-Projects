"""
Water Drinking Reminder:
------------
Using tkinker as ui to remind 
user every hour for drinking 
water

messagebox -- from tkinter to show notification
time -- module to schedule the message every one hour
"""
import time
from tkinter import messagebox

def reminder():
    messagebox.showwarning("Reminder", "Please Drink A glass of Water")
    
while True:
    reminder()
    time.sleep(60*60)
