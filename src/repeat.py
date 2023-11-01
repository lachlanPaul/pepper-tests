# I hate this API
# Update: I fixed it, I hate it slightly less now :)
# Update: nvm
# Yet another update: Taking reference from some randoms repo, let's hope it works
from __future__ import print_function  # This is so I can use end in my print statements

import time

from naoqi import ALProxy

IP = "192.168.1.58"
PORT = 9559
FILEPATH = "/home/nao/lachlan/recordings/repeat.wav"

tts = ALProxy("ALTextToSpeech", IP, PORT)
audio = ALProxy("ALAudioDevice", IP, PORT)
record = ALProxy("ALAudioRecorder", IP, PORT)
play = ALProxy("ALAudioPlayer", IP, PORT)


# Honestly just hoping this works
def main():
    global tts, audio, record, play  # Because Python likes to change its mind on whether it needs this or not

    print("Giving instructions", end="\r")
    tts.say("You have 10 seconds to speak. Recording begins now.")

    print("Recording audio", end="\r")
    record.startMicrophonesRecording(FILEPATH, "wav", 16000, (0, 0, 1, 0))
    time.sleep(10)  # Really hope this doesn't shut down the actual recording that's happening (I miss asyncio)

    print("Finished recording audio", end="\r")
    record.stopMicrophonesRecording()

    tts.say("This is your recording!")
    print("Playing recording", end="\r")
    play.playFile(FILEPATH, 0.5, 1.0)


if __name__ == '__main__':
    main()
