#Modules

from random import random
import sys

filemode = False

print("* Launcher 2022")

#File Checker

try:
    file = sys.argv[1]
    if file.endswith(".ast"):
        filemode = True
except IndexError:
    pass

#Manual Interpreter

if filemode == False:
    while True:
        cmd = input("*> ")
        if cmd == "*":
            print("Hello World")
        elif cmd == " * ":
            print(random() * 2147483647)
        elif cmd == "*+*":
            while True:
                pass

        elif cmd.startswith("run"):
            cmd, file = cmd.split(" ", 1)
            with open(file) as f:
                for cmd in f:
                    print(cmd)
                    cmd = cmd.replace("\n", " ")
                    if cmd == "*":
                        print("Hello World")
                    elif cmd == " * ":
                        print(random() * 2147483647)
                    elif cmd == "*+*":
                        while True:
                            pass

#File Mode Interpreter


if filemode == True:
    with open(file) as f:
        for cmd in f:
            print(cmd)
            if cmd == "*":
                print("Hello World")
            elif cmd == " * ":
                print(random() * 2147483647)
            elif cmd == "*+*":
                while True:
                    pass
