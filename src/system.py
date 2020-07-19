# Written by Rabia Alhaffar in 17/July/2020
# PyJoy system part
from os import *
from sys import *
from platform import *
from urllib.parse import urlparse
from zipfile import ZipFile

python_version = int(sys.version[0])

def get_os():
    if "win" in sys.platform or sys.platform == "cygwin" or sys.platform == "msys":
        return "Windows"

    elif "darwin" in sys.platform:
        return "Mac"
    
    elif "linux" in sys.platform:
        return "Linux"

    elif "os2" in sys.platform:
        return "OS/2"

    elif "freebsd" in sys.platform:
        return "FreeBSD"

    elif "openbsd" in sys.platform:
        return "OpenBSD"

    else:
        return sys.platform

def execute(cmds):
    return os.system(cmds)

def download(src, dist):
    url = urlparse(src)
    ddist = os.path.basename(url.path)
    if os.system("curl --version") == 0:
        if not os.system("cd %s" % dist) == 0:
            os.system("mkdir %s" % dist)
        os.system("curl -o %s\%s %s" % (dist, os.path.basename(ddist), src))

def extract(src, dist):
    with ZipFile(src, "r") as archive:
        archive.extractall(dist)

def current_directory():
    return os.path.dirname(os.path.realpath(__file__))

def run(python_file):
    os.system("python " + python_file)
