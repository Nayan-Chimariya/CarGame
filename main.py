import GameFiles
import features

command = ""
state = "stopped"

def main():
  is_start = input("Press [Enter] to start ").upper()
  if is_start == "":
    GameFiles.loadingScreen()
  
  commands = {
    "help" : GameFiles.help,
    "start" : features.start,
    "accelerate" : features.accelerate,
    "break" : features.pause,
    "stop" : features.stop
  }

main()
