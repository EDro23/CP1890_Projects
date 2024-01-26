#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:44:11 2024

@author: kaileyslaney
"""

import baseballPlayer from baseball_game_spyder

def divider():
    print(50 * "=")
def menutop(gamedayinput=None):
    print("\t\t\t\tBaseball Team Manager").
    print()
    print("CURRENT DATE:", datetime.datetime.now())
    print(f"GAME DATE: {gamedayinput}")
    print("Days until next game:", gamedayinput)
    print()

def menu_options():
    print("MENU OPTIONS")
    print("1 - Display lineup"
          "2 - Add player"
          "3 - Remove player"
          "4 - Move player"
          "5 - Edit player position"
          "6 - Edit player stats"
          "7 - Exit program\n")

def positions():
    print("POSITIONS")
    print("C, 1B, 2B, 3B, SS, LF, CF, RF, P")

def main():
    divider()
    menutop()
    menu_options()
    positions()
    divider()
    option = input("Menu option: ")
    if option == "1":
        self.displaylineup

if __name__ == "__main__":
    main()