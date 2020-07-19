# Written by Rabia Alhaffar in 17/July/2020
# PyJoy audio part,Runs on OpenAL
# You can also use OpenAL functions if you want
from openal import *
from openal.al import *
from openal.alc import *

# Deinitialize OpenAL automatically for better control
oalSetAutoInit(False)

# NOTES: OGG and WAV are only supported!
# To manipulate,See link below
# https://github.com/Zuzu-Typ/PyOpenAL#reference-for-pyopenals-own-classes-and-functions
class audio:
    def __init__(self, src, audio_type):
        if audio_type == "sound":
            if openal_initialized():
                return oalOpen(src)
        if audio_type == "music":
            if openal_initialized():
                return oalStream(src)

    def playing(self):
        return self.get_state() == AL_PLAYING


def openal_initialized():
    return oalGetInit()

def init_openal():
    if not openal_initialized():
        oalInit()

def close_openal():
    if openal_initialized():
        oalQuit()

def audio_device():
    return oalGetDevice()

def audio_context():
    if openal_initialized():
        return oalGetContext()
