"""
    Takes a photo, then displays it on the screen

    Lachlan Paul, 2023
"""
import time

from naoqi import ALProxy

IP = "192.168.1.58"
PORT = 9559

photoCapture = ALProxy("ALPhotoCapture", IP, PORT)
tablet = ALProxy("ALTabletService", IP, PORT)
tts = ALProxy("ALTextToSpeech", IP, PORT)


def main():
    photoCapture.setPictureFormat("jpg")
    photoCapture.takePictures(1, "/home/nao/lachlan/photo/capture.jpg", "image")
    print("Image taken")

    # If this doesn't work try these:
    # tablet.showImage("http://198.18.0.1/lachlan/photo/capture.jpg")
    # tablet.showImage("http://{}/lachlan/photo/capture.jpg".format(IP))
    tablet.showImage("/home/nao/lachlan/photo/capture.jpg")
    print("Image displayed")
    tts.say("Do you like this photo I took?")

    time.sleep(5)

    tablet.hideImage()
