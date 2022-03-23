import os
import sys
import subprocess

if sys.platform == "win32":
    os.system('cls')
else:
    os.system('clear')

print("CariboSystem Recovery Tool v0.0.1")
print()
print("Select System:")
print("\t 1) CariboSystem 6.0.4")
print("\t 2) CariboSystem 6.0.5")
print("\t 3) CariboSystem 6.1.0")
print("\t 4) CariboSystem 6.11.0")
print()
value = ""
while value != "quit" or value != "exit":
    value = input("> ").lower()
    if value == "1":
        print("System Image Unavailable..!")
    elif value == "2":
        print("System Image Unavailable..!")
    elif value == "3":
        print("System Image Link will be Activated Soon...!")
    elif value == "4":
        print("System Under Development, Image will be out Soon....!")
    elif value == "5" or value == "quit" or value == "exit":
        break
    else:
        print("Invalid Response.!")