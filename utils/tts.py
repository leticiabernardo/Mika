import time

# import pyttsx
import pyttsx3
from gtts import gTTS

from utils.player import Player


class Tts:
    def __init__(self):
        self.my_player = Player()
        self.file = "files/audio/"
        self.audio_file = "audio.mp3"

    def generate_file(self, text):
        voz = gTTS(text, lang="pt")
        voz.save(self.file + self.audio_file)

        return self.file + self.audio_file

    def gtts_speak(self, text):
        file_to_read = self.generate_file(text)

        time.sleep(1)
        self.my_player.play(file_to_read)

    def pyttsx_speak(self, text):
        en = pyttsx3.init()
        en.setProperty('voice', b'brazil+m3')

        en.say(text)
        en.runAndWait()

    # define default method speak
    def speak(self, text):
        self.pyttsx_speak(text)
