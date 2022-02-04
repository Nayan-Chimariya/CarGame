state = "stopped"

def start():
  global state
  if state == "started":
    print("The car is already started, dumass!\n")
  else:
    print("The car has now started\n")
    state = "started"

def accelerate():
  print("work in progress")

def gear():
  print("work in progress")

def pause():
  print("work in progress")

def fire():
  print("work in progress")

def stop ():
  global state
  if state == "stopped":
      print("The car is already stopped, dumass!\n")

  else:
    print("The car is now stopped\n")
    state = "stopped"
