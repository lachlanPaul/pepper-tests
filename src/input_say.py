"""
    Simply says what's given as input into the Python terminal

    Lachlan Paul, 2023
"""
from naoqi import ALProxy
from src.common.ip_port import IP, PORT

tts = ALProxy("ALTextToSpeech", IP, PORT)

usr_input = input("Make Pepper say: ")
tts.say(usr_input)
