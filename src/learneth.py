import os
import json
import sys

def cls(): os.system(['clear', 'cls'][os.name in ('nt', 'dos')])

def getKeys(dic):
    return [*dic]

def menu(options: dict, sub=False):
    while True:
        cls()
        if sub:
            print("0: Back\n")
        else:
            print("0: Quit\n")
        for i, option in enumerate(options):
            print(str(i+1) + ": " + option)
        choice = input("\n>")
        try:
            choice = int(choice)
            if choice == 0:
                return None
            selected = options[getKeys(options)[choice-1]]
            if type(selected) == dict:
                text = menu(selected, sub=True)
                if text is not None:
                    help_mode(text)
            else:
                help_mode(selected)
        except ValueError:
            pass
        except IndexError:
            pass

def help_mode(text):
    stop_index = 0
    full_text = text.split()
    while True:
        cls()
        print(" ".join(full_text[:stop_index]) + "\n")
        print("\n" + ["ENTER: Another word", "No more words"][stop_index>=len(full_text)])
        print("""B: Go back one word
R: Clear the words
Q: Return to the menu""")
        choice = input("> ").lower()
        if choice == "":
            stop_index += (stop_index!=len(full_text))
        elif choice == "b":
            stop_index += (stop_index==0)-1
        elif choice == "r":
            stop_index = 0
        elif choice == "q":
            return

if __name__ == "__main__":
    if len(sys.argv) == 2:
        try:
            try:
                MENU_OPTIONS = json.load(open(sys.argv[1]))
                menu(MENU_OPTIONS)
                sys.exit()
            except IsADirectoryError:
                print("Error: expected valid JSON file, recieved directory")
            except json.decoder.JSONDecodeError:
                print("Error: expected valid JSON file, recieved otherwise")
        except Exception:
            print("Unhandled exception occurred!")
        
    else:
        print("Error: Exactly one argument expected")
