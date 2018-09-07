from utils.tts import Tts


class Oran:
    def __init__(self):
        self.tts = Tts()

    def call_my_name(self):
        self.tts.speak("Pois não")

    def get_my_name(self):
        self.tts.speak("Meu nome é Oran")