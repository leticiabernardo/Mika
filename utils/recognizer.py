import speech_recognition as sr


class Recognizer:
    def __init__(self):
        self.rec = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as fala:
            text_recognize = self.rec.listen(fala)

        try:
            text = self.rec.recognize_google(text_recognize, language='pt')
            return "response", text

        except sr.UnknownValueError:
            return "error-listen", "Não entendi o que você disse. Vamos tentar novamente?"