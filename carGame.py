# This is a simple car game.
# The program takes input of 3 commands (start, stop and quit) from the user to play the game. 

started = False

while True:
    command = input("> ").upper()
    if command == "START":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started...Ready to go!")
    elif command == "STOP":
        if not started:
            print("Car is already stopped.")
        else:
            started = False
            print("Car stopped")
    elif command == "QUIT":
        break
    elif command == "HELP":
        print("""
start - to start the car
stop - to stop the car
quit - to exit""")
    else:
        print("I don't understand...")
