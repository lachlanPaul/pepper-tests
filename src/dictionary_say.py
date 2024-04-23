"""
    Reads out meanings from a dictionary

    Lachlan Paul, 2023
"""
from naoqi import ALProxy
from src.common.ip_port import IP, PORT

words = {
    "run": "move at a speed faster than a walk, never having both or all the feet on the ground at the same time."
}

tts = ALProxy("ALTextToSpeech", IP, PORT)

for word, definition in words.items():
    tts.say("The definition of", word, "is", definition)
