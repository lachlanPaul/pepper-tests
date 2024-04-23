"""
    Test for .mp3 capability

    Lachlan Paul, 2023    
"""
import time

from naoqi import ALProxy
from src.common.ip_port import IP, PORT

play = ALProxy("ALAudioPlayer", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)


def main():
    global tts, play

    tts.say("Time for my special move!")
    time.sleep(2)
    play.playFile("/home/nao/lachlan/dp.mp3", 0.5, 1.0)  # Plays Ryu's "Shoryuken!" sfx from SFII

if __name__ == '__main__':
    main()