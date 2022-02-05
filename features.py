state = "stopped"
gear = 1
max_acceleration = 30

def start():
  global state
  if state == "started":
    print("The car is already started, dumass!\n")
  else:
    print("The car has now started\n")
    state = "started"

def accelerate():
  global state
  if state == "stopped":
    print("Start the car first\n")
  else:
    acc_value = int(input("Enter speed in meter per second: "))
    if acc_value > max_acceleration:
      print("Increase gear to reach that speed\n")
    else:
      print(f"Accelerating at {acc_value} m/s\n")
    

def gear():
  global max_acceleration
  gear_level = int(input("Enter gear level: "))
  gears = {
    1 : 30,
    2 : 60,
    3 : 90,
    4 : 120,
    5 : 150,
    6 : 180
    }
  max_acceleration = gears[gear_level] if gear_level in gears else print("\nInvalid")
  print (f"{max_acceleration} is now your maximum acceleration\n")

def fire():
  print("work in progress")

def stop ():
  global state
  if state == "stopped":
      print("The car is already stopped, dumass!\n")

  else:
    print("The car is now stopped\n")
    state = "stopped"
