# This is a sample Python script.
import random
import csv
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')



f = open('playingdays.csv','r')

from csv import DictReader

from typing import List, Dict

file_handle = open('playingdays.csv','r')
csv_reader = DictReader(file_handle)
table: List[Dict[str, int]] = []

for row in csv_reader:
    if row["1"] == "checked":
       Player = row["Player"]
       Rating = int(row["Rating"])
       print('Player {} has a rating of {}'.format(Player, Rating))

file_handle.close()


#Learned about randomizing and shuffling and lists
#need to learn how to remove items from list?
#https://datagy.io/python-shuffle-list/#:~:text=Let%E2%80%99s%20take%20a%20look%20at%20how%20we%E2%80%99ve%20managed,as%20the%20length%20of%20the%20list%20may%20change.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
