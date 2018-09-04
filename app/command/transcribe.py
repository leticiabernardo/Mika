import clipboard
from googletrans import Translator

from app.file_manager.make_txt import MakeTxt
from utils.recognizer import Recognizer
from utils.tts import Tts


class Transcribe:
    def __init__(self):
        self.tts = Tts()
        self.rec = Recognizer()
        self.make_txt = MakeTxt()
        self.translator = Translator()


    def transcribe(self):
        self.tts.speak("Pode falar e eu escreverei")
        text_listen = self.rec.listen()

        if text_listen[0] == 'error':
            self.tts.speak("Me desculpe mas não compreendi o que disse")

        else:

            self.tts.speak("Aqui está!")
            print(text_listen[1])

            self.tts.speak("Deseja copiar para a área de transferência?")
            text_listen_resp = self.rec.listen()

            if text_listen_resp[1].upper() == 'SIM':
                my_text = text_listen[1]
                clipboard.copy(my_text)

                self.tts.speak("Pronto! Copiado para a área de transferência!")

                self.make_txt.save_data("transcribes", text_listen[1])
                self.tts.speak("Também tomei a liberdade de salvar esta transcrição, procure na pasta files")


    def translate(self):
        self.tts.speak("O que deseja traduzir para o inglês?")
        text_listen = self.rec.listen()

        if text_listen[0] == 'error':
            self.tts.speak("Me desculpe mas não compreendi o que disse")

        else:
            translated_text = (self.translator.translate(text_listen[1], dest='en')).text

            self.tts.speak("Aqui está!")
            print(translated_text)

            self.tts.speak("Deseja copiar para a área de transferência?")
            text_listen_resp = self.rec.listen()

            if text_listen_resp[1].upper() == 'SIM':
                clipboard.copy(translated_text)

                self.tts.speak("Pronto! Copiado para a área de transferência!")

                self.make_txt.save_data("translates", text_listen[1] + "|" + translated_text)
                self.tts.speak("Também tomei a liberdade de salvar esta tradução, procure na pasta files")
