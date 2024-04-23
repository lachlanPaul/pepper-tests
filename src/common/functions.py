from naoqi import ALProxy
from src.common.ip_port import IP, PORT

TTS = ALProxy("ALTextToSpeech", IP, PORT)
PHOTOCAPTURE = ALProxy("ALPhotoCapture", IP, PORT)
TABLET = ALProxy("ALTabletService", IP, PORT)
# ANIMATION = session.service("ALAnimationPlayer")
ANIMATION = ALProxy("ALAnimationPlayer", IP, PORT)