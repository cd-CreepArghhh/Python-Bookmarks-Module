import sys
import os

path = None


def get_lib_path():
    global path
    for pathItem in sys.path:
        if pathItem.endswith(r"\lib"):
            path = pathItem
            return


print("[Information] Getting Path...")

get_lib_path()

path += r"\site-packages"


print("[Information] Creating module...")

f = open(path + r"\bookmarks.py", "w")
program = open("bookmarks.py", "r")
f.writelines(program.readlines())
f.close()

open(path + r"\__pycache__\Bookmarks.txt", "w").close()

delete = input("Would you like to delete the installer? Y/N: ").lower()
if delete == "y":
    os.remove("Bookmarks Installer.py")
