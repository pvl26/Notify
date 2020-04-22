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
from multiprocessing import Process

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
        data_set = ["Marie_Curie", "Audrey_Hepburn", "Grace_Hopper", "Katherine_Johnson", "J._K._Rowling", "Margaret_Hamilton_(om_de_știință)", "Elisa_Leonida_Zamfirescu"]
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
    
    def getDestinations(self):
        self.type = "Beautiful places:"

        # data set for the urls used for notifications
        data_set = ["Madrid", "Barcelona", "Roma", "Sankt_Petersburg", "Veneția", "Lisabona", "München", "Budapesta"]
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
    choice = random.choice([0, 1, 2])
    # choice = 2
    if choice == 0 :
        return Culture().getMusic()
    if choice == 1 :
        return Culture().getWoman()
    if choice == 2 :
        return Culture().getDestinations()

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

#  Health_Water notification module
def Health_Water():
    Notify.init("Test")

    while True:
        time.sleep(10)  # sleep for 1800 seconds

        content = Health().Water()
        notification = Notify.Notification.new(
            content.type,
            content.info
        )
        notification.set_urgency(0)
        notification.show()
    
    Notify.uninit("Test")

#  Health_Fruit notification module
def Health_Fruit():
    Notify.init("Test")

    while True:
        time.sleep(22)  # sleep for 5400 seconds

        content = Health().Fruit()
        notification = Notify.Notification.new(
            content.type,
            content.info
        )
        notification.set_urgency(0)
        notification.show()

    Notify.uninit("Test")

#  Health_Pause notification module
def Health_Pause():
    Notify.init("Test")

    while True:
        time.sleep(47)  # sleep for 3600 seconds

        content = Health().Pause()
        notification = Notify.Notification.new(
            content.type,
            content.info
        )
        notification.set_urgency(0)
        notification.show()

    Notify.uninit("Test")

#  Culture notification module
def Culture_notification():
    Notify.init("Test")

    while True:   
        time.sleep(55)  # sleep for 10000 seconds

        content = getCultureNotification()
        notification = Notify.Notification.new(
            content.type,
            content.info
        )
        notification.set_urgency(0)
        notification.show()

    Notify.uninit("Test")


def main():

    H_W = Process(target=Health_Water)
    H_W.start()
    
    H_F = Process(target=Health_Fruit)
    H_F.start()
    
    H_P = Process(target=Health_Pause)
    H_P.start()

    C = Process(target=Culture_notification)
    C.start()

    H_W.join()
    H_F.join()
    H_P.join()
    C.join()




if __name__ == "__main__":
    main()
