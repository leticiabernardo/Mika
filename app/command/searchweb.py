import webbrowser as wb

from app.file_manager.make_txt import MakeTxt
from utils.recognizer import Recognizer
from utils.tts import Tts


class SearchWeb:
    def __init__(self):
        self.chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
        self.search = ""
        self.tts = Tts()
        self.rec = Recognizer()

    def search_in_gooogle(self):
        self.tts.speak("O que deseja pesquisar no Google?")
        text_listen_search = self.rec.listen()

        if text_listen_search[0] == "error":
            self.tts.speak(text_listen_search[1])
        else:
            self.tts.speak("Abrindo sua pesquisa no navegador...")

            try:
                wb.get(self.chrome_path).open("https://www.google.com.br/search?q=" + text_listen_search[1] + "&cad=h")
            except Exception as e:
                print(e)

    def search_site(self):
        self.tts.speak("Diga o site que deseja abrir?")
        text_listen_search = self.rec.listen()

        if text_listen_search[0] == "error-listen":
            self.tts.speak(text_listen_search[1])
        else:
            self.tts.speak("Abrindo seu link no navegador...")

            try:
                wb.get(self.chrome_path).open(text_listen_search[1])
            except Exception as e:
                print(e)

            self.tts.speak("Deseja salvar?")
            text_listen_save = self.rec.listen()
            print(text_listen_save)
            command_text = text_listen_save[1].upper()

            get_out = False
            while text_listen_save[0] == "error" or get_out == False:

                if command_text == 'SIM':
                    self.tts.speak("Diga um nome para sempre poder chamar esta página")
                    text_listen_name = self.rec.listen()

                    if text_listen_save[0] == 'response':
                        my_data = text_listen_name[1] + "|" + text_listen_search[1] + "\n"

                        print(my_data)
                        make_txt = MakeTxt()

                        make_txt.save_data("pages", my_data)

                get_out = True
