# Write a Python program to display the current date and time.
# This is the way I wrote it
date = input("enter the year, month and day presently in this format: The Year-The month-The day")
time = input("enter the time right now in this format : Hours-Minutes-Seconds")
print("Current date and time : ", date, time)
# This is the way it is in the python solution
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))
