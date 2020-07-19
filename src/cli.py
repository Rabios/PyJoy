# Written by Rabia Alhaffar in 17/July/2020
# PyJoy CLI, You can run your games even like if it were LÖVE
# You can also add your own commands
from os import *
from sys import *
from platform import *

# List of packages used by PyJoy
pyjoy_packages = [
    "PyOpenGL",
    "PyOpenGL_accelerate",
    "PyOpenAL",
    "PyOGG",
    "GLFW",
    "Pillow",
    "freetype-py"
]

if use_cli:
    # Check arguments,If not find folder called "game" and run main.py
    if len(sys.argv) > 1:
        if "-v" in sys.argv or "--version" in sys.argv:
            print(pyjoy_version)
        elif "-p" in sys.argv or "--platform" in sys.argv:
            print(get_os())
        elif "-l" in sys.argv or "--packages" in sys.argv:
            for p in pyjoy_packages:
                print(p)
        elif "test" in sys.argv:
            if os.system("cd sample") == 0:
                os.system("python game\main.py")
        else:
            os.system("python " + (sys.argv[1] + "\main.py"))
    else:
        if os.system("cd game") == 0:
            os.system("python game\main.py")
