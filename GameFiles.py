import os
from random import randint

def help():
  print("These are my commands:\n"
            "----------------------\n"
            "1. start - to start the car\n"
            "2. stop - to stop the car\n"
            "3. exit - to exit the program\n")

def goal():
  goal = (randint(1000,10000))
  print("Your goal is to reach{goal} within {time_limit} seconds}")

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