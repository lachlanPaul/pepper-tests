"""
    Reads out meanings from a dictionary

    Lachlan Paul, 2023
"""
from naoqi import ALProxy

words = {
    "run": "move at a speed faster than a walk, never having both or all the feet on the ground at the same time."
}

IP = "192.168.1.58"
PORT = 9559

tts = ALProxy("ALTextToSpeech", IP, PORT)

for word, definition in words.items():
    tts.say("The definition of", word, "is", definition)
