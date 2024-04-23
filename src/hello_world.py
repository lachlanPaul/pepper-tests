from naoqi import ALProxy
from src.common.ip_port import IP, PORT
tts = ALProxy("ALTextToSpeech", IP, PORT)
tts.say("Hello, world!")