#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:42:42 2024

@author: kaileyslaney
"""
from dataclass import dataclasses
import string
from datetime import datetime



@dataclass

class baseballPlayer:
    __firstname: string.ascii_uppercase
    __lastname:  string.ascii_uppercase
    __position:  string.ascii_uppercase
    __at_bats:  int = 0
    __hits:  int = 0
    __average:  int = 0

    def current_date(self):
        return datetime

    def displaylineup(self):
        for i, row in enumerate(self):
            print(f"{self.__firstname} "
                  f"{self.__lastname}\t\t\t\t"
                  f"{self.__position}\t"
                  f"{self.__at_bats}"
                  f"\t{self.__hits}")

    def gamedayinput(self):
        userinput = input("Enter your gameday!(yyyy-mm-dd) ")
        return userinput.split('-')
