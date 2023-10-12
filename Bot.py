import keyboard
import time
import pyfiglet

def Main():
    Title = pyfiglet.figlet_format("Demins autosend")

    print(f"{Title}")
    Message = str(input("What would you like to send? "))
    
    while True:
        Delay = input("Delay in seconds? ")
    
        try:
            Delay = int(Delay)
            break
        except ValueError:
            print("The delay is not a valid integer.")
    
    def AutoSend():
        print("\nStarting script in 3s...")
        time.sleep(3)
        print("Running")
        while True:
            keyboard.write(Message)
            keyboard.send("enter")
            print("Typed message")
            time.sleep(Delay)
    
    Start = input("\nWould you like to start the script..? (Y/N) ")
    if Start.lower() == "y":
        AutoSend()
    else:
        return
        
Main()