import os
from random import randint
import progressbar
from time import sleep

def help():
  print("These are my commands:\n"
            "----------------------\n"
            "1. start - to start the car\n"
            "2. stop - to stop the car\n"
            "3. exit - to exit the program\n")

def goal():
  global time_limit
  distance = (randint(100,1000))
  time_limit = 10
  print(f"Your goal is to reach {distance} km within {time_limit} seconds\n")

def loadingScreen():
  os.system("cls")
  title = "\n-------------------\nWelcome to car game\n-------------------\n"
  print(title)
  
  how_to_play = ("using the cars feature, reach the goal\n")
  print(how_to_play)

  car_art = ('''
        ___..............._
              __.. ' _'.""""""\\""""""""- .`-._
  ______.-'         (_) |      \\           ` \\`-. _
  /_       --------------'-------\\---....______\\__`.`  -..___
  | T      _.----._           Xxx|x...           |          _.._`--. _
  | |    .' ..--.. `.         XXX|XXXXXXXXXxx==  |       .'.---..`.     -._
  \_j   /  /  __  \  \        XXX|XXXXXXXXXXX==  |      / /  __  \ \        `-.
  _|  |  |  /  \  |  |       XXX|""'            |     / |  /  \  | |          |
  |__\_j  |  \__/  |  L__________|_______________|_____j |  \__/  | L__________J
      `'\ \      / ./__________________________________\ \      / /___________\
          `.`----'.'   dp                                `.`----'.'
            `""""'                                         `""""'
  ''')
  print(car_art)

def ProcessBar():  
  bar = progressbar.ProgressBar(maxval=20, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
  bar.start()
  for i in range(20):
    bar.update(i+1)
    sleep(0.25)
  bar.finish()

def EndScreen():
   print("Time Limit Reached")
   ''' handle: win/loss? .. high score .. re run? '''