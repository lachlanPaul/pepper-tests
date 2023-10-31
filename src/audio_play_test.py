# Test for .mp3 capability
import time

from naoqi import ALProxy

IP = "192.168.1.58"
PORT = 9559

play = ALProxy("ALAudioPlayer", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)


def main():
    global tts, play
    tts.say("Time for my special move!")
    time.sleep(2)
    play.playFile("src/resource/dp.mp3", 0.5, 1.0)  # Plays Ryu's "Shoryuken!" sfx from SFII

if __name__ == '__main__':
    main()