import os
import GameFiles
import features
import threading
from time import sleep

game_running = False
state = "stopped"

time_limit = 10
def TimeLimit():
  global game_running 
  for time in range(0,time_limit):
    sleep(2)
    time += time
    if time == time_limit:
      game_running = False
      return game_running
      
def main():
  global game_running
  is_start = input("Press [Enter] to start ").upper()
  if is_start == "":
    game_running = True
    GameFiles.loadingScreen()
  
  print("\nTighten your seat belt the game starts at...")
  GameFiles.ProcessBar()
  os.system("cls")

  GameFiles.goal()
  while game_running == True:
    command = input("> ")

    commands = {
    "help"       : GameFiles.help,
    "start"      : features.start,
    "gear"       : features.gear,
    "accelerate" : features.accelerate,
    "fire"       : features.fire,
    "stop"       : features.stop,
    "exit"       : exit
    }

    commands[command]() if command in commands else print("\nInvalid")

  if(game_running == False):
    GameFiles.EndScreen()

threading.Thread(target = TimeLimit).start()
threading.Thread(target = main).start()