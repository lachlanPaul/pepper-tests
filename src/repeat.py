# I hate this API
# Update: I fixed it, I hate it slightly less now :)
# Update: nvm
import asyncio
import time

from naoqi import ALProxy

IP = "192.168.1.58"

speech_record = ALProxy("ALAudioRecorder", IP, 9559)  # Audio record
audio_play = ALProxy("ALAudioPlayer", IP, 9559)  # Audio player
tts = ALProxy("ALTextToSpeech", IP, 9559)  # TTS

tts.say("You have 10 seconds to speak. Recording begins now.")
speech_record.startMicrophoneRecording()
time.sleep(10)
speech_record.stopMicrophoneRecording()
