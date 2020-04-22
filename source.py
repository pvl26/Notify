#!/usr/bin/env python3

import re
import random
import requests
import bs4
from bs4 import BeautifulSoup
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import os
import time

class Culture:
    # method to clear input_str of nested parentheses with stuff in between them
    # copyright: https://stackoverflow.com/a/14598135
    def clearContent(self, input_str):
        ret = ''
        skip1c = 0
        skip2c = 0
        for i in input_str:
            if i == '[':
                skip1c += 1
            elif i == '(':
                skip2c += 1
            elif i == ']' and skip1c > 0:
                skip1c -= 1
            elif i == ')'and skip2c > 0:
                skip2c -= 1
            elif skip1c == 0 and skip2c == 0:
                ret += i
        return ret

    def getMusic(self):
        self.type = "Music curiosities:"

        #  data set for the urls used for notifications
        data_set = ["Nai", "Chitară", "Pian"]
        # TO DO: add more to dataset

        #  get a randome url source
        url = "https://ro.wikipedia.org/wiki/" + random.choice(data_set)
        source = requests.get(url).text
        bs = BeautifulSoup(source, "lxml")

        #  get the content to put in the notification
        content = bs.p.text
        content = self.clearContent(content)

        self.info = content
        return self

    def getWoman(self):
        self.type = "Imortant woman:"

        # data set for the urls used for notifications
        data_set = ["Marie_Curie"]
        # TO DO: add more to data_set

        # get a randome url source
        url = "https://ro.wikipedia.org/wiki/" + random.choice(data_set)
        source = requests.get(url).text
        bs = BeautifulSoup(source, "lxml")

        # get the content to put in the notification
        content = bs.p.text
        content = self.clearContent(content)

        self.info = content
        return self

    # TO DO: add more notification content scrapping methods

def getCultureNotification():
    #  choose randomly the notification type
    choice = random.choice([0, 1])
    # choice = 1
    if choice == 0 :
        return Culture().getMusic()
    if choice == 1 :
        return Culture().getWoman()

    #  TO DO(optional): don't repeat a previous shown notification


class Health:
    def Water(self):
        self.type = "Hidrate!"
        self.info = "It's recomended to drink a glass of water every 30 minutes."
        return self

    def Fruit(self):
        self.type = "Eat a fruit!"
        self.info = "Take your portion of Vitamin C"
        return self

    def Pause(self):
        self.type = "Break time!"
        self.info = "You shouldn't spend more than an hour on the chair!"
        return self

def main():
    Notify.init("Test")
    
    #  Health_Water module
    # while True:
    #     time.sleep(10)  # sleep for 1800 seconds

    #     content = Health().Water()
    #     notification = Notify.Notification.new(
    #         content.type,
    #         content.info
    #     )
    #     notification.set_urgency(0)
    #     notification.show()

    #  Health_Fruit module
    # while True:
    #     time.sleep(10)  # sleep for 1800 seconds

    #     content = Health().Fruit()
    #     notification = Notify.Notification.new(
    #         content.type,
    #         content.info
    #     )
    #     notification.set_urgency(0)
    #     notification.show()

    #  Health_Pause module
    # while True:
    #     time.sleep(10)  # sleep for 1800 seconds

    #     content = Health().Pause()
    #     notification = Notify.Notification.new(
    #         content.type,
    #         content.info
    #     )
    #     notification.set_urgency(0)
    #     notification.show()

    #  Culture notification module
    while True:   
        time.sleep(5)  # sleep for 5400 seconds

        content = getCultureNotification()
        notification = Notify.Notification.new(
            content.type,
            content.info
        )
        notification.set_urgency(0)
        notification.show() 
        

    Notify.uninit("Test")

if __name__ == "__main__":
    main()
