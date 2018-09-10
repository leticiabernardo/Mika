from utils.tts import Tts
import sys


class Basic:
    def __init__(self):
        self.tts = Tts()

    def hello(self):
        self.tts.speak("Olá!! Sou a Mika.")

    def goodbye(self):
        self.tts.speak("Me sinto grata por poder servir. Até mais!")
        sys.exit(0)

    def i_gonna_help_you(self):
        self.tts.speak("Em que posso ajudar?")

    def i_cant_understand(self):
        self.tts.speak("Não entendi o que disse")

    def silence_mode(self):
        self.tts.speak("Entrando no modo silencioso. " +
                       "Basta me chamar e eu retornarei")
