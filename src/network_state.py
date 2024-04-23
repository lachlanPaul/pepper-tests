"""
    Prints the robot's connection status

    Lachlan Paul, 2023
"""

from naoqi import ALProxy
from src.common.ip_port import IP, PORT

network = ALProxy("ALConnectionManager", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)

if network.state == "online":
    tts.say("I am connected and online")
elif network.state == "offline":
    tts.say("I am offline")  # :(
