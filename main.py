import GameFiles
import features

command = ""
state = "stopped"

def main():
  is_start = input("Press [Enter] to start ").upper()
  if is_start == "":
    IsGAmeRunning = True
    GameFiles.loadingScreen()
  
  while IsGAmeRunning == True:
    command = input("> ")

    commands = {
    "help" : GameFiles.help,
    "start" : features.start,
    "accelerate" : features.accelerate,
    "break" : features.pause,
    "stop" : features.stop
    }

    commands[command]() if command in commands else print("\nInvalid")

main()
