"""
    Prints the robot's connection status

    Lachlan Paul, 2023
"""

from naoqi import ALProxy

IP = "192.168.1.58"
PORT = 9559

network = ALProxy("ALConnectionManager", IP, PORT)
tts = ALProxy("AlTextToSpeech", IP, PORT)

if network.state == "online":
    tts.say("I am connected and online")
elif network.state == "offline":
    tts.say("I am offline")  # :(
