import sys, termios, tty, os, time
 
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
def manual_mode():
    button_delay = 0.2
    print("program started")
    while(True):
        char = getch()
 
        if (char == "a"):
            print("left")
            time.sleep(button_delay)
    
        if (char == "s"):
            print("back")
            time.sleep(button_delay)
    
        elif (char == "d"):
            print("right")
            time.sleep(button_delay)
    
        elif (char == "w"):
            print("forward")
            time.sleep(button_delay)

        elif (char == "p"):
            print("up")
            time.sleep(button_delay)

        elif (char == "l"):
            print("down ")
            time.sleep(button_delay)
        
        elif (char == "0"):
            break

def main():
    while(True):
        print("what mode to run? Auto or Manual")
        x = input()
        if x=="Auto":
            print("auto mode selected.")
            #put auto mode function here.
        if x== "Manual":
            manual_mode()






if __name__ == "__main__":
    main()