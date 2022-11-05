#Modules

from random import random
import sys

filemode = False
cmd = ""

print("* Launcher 2022")

#File Checker

try:
    file = sys.argv[1]
    if file.endswith(".ast"):
        filemode = True
    else:
        raise IndexError
except IndexError:
    pass

#Manual Interpreter


while True:
    if filemode == False:
        cmd = input("*> ")
        if cmd == "*":
            print("Hello World")
        elif cmd == " * ":
            print(random() * 2147483647)
        elif cmd == "*+*":
            while True:
                pass

    #File Mode Interpreter

    elif cmd.startswith("run") or filemode == True:
        if filemode == False:
            cmd, file = cmd.split(" ", 1)

        with open(file) as f:
            for cmd in f:
                cmd = cmd.replace("\n", "")
                if cmd == "*":
                    print("Hello World")
                elif cmd == " * ":
                    print(random() * 2147483647)
                elif cmd == "*+*":
                    while True:
                        pass

        if filemode == True:
            break
