__author__ = "foxx"
__email__ = "leticiaellenbernardo@gmail.com"
__version__ = "0.0.22"
__license__ = "MIT"
__status__ = "Beta"

import sys

from app.command.datetime import ComDateTime
from app.command.meteorology import Meteorology
from app.command.quotation import Quotation
from app.command.searchweb import SearchWeb
from app.command.transcribe import Transcribe
from app.data_mining.DMTwitter.dm_twitter import DMTwitter
from app.data_mining.DMWikipedia.dm_wikipedia import DMWikipedia
from utils.recognizer import Recognizer
from utils.tts import Tts

print("Iniciando...")

tts = Tts()
rec = Recognizer()
com_datetime = ComDateTime()
search_web = SearchWeb()
quo = Quotation()
met = Meteorology()
transcribe = Transcribe()
twitter = DMTwitter()
wikipedia = DMWikipedia()

tts.speak("Olá!! Aqui é a Oran.")


while True:
    tts.speak("Diga um comando")
    text_listen = rec.listen()
    command_text = text_listen[1].upper()

    print("Você disse: " + command_text)

    if command_text == "ORAN":
        tts.speak("Pois não?")

    elif command_text == "PESQUISAR NO GOOGLE":
        search_web.search_in_gooogle()

    elif command_text == "ABRIR SITE":
        search_web.search_site()

    elif command_text == "QUE HORAS SÃO":
        com_datetime.getTime()

    elif command_text == "QUE DIA É HOJE":
        com_datetime.getDate()

    elif command_text == "COMO ESTÁ O TEMPO":
        met.getMeteorology()

    elif command_text == "COMO ESTÁ A COTAÇÃO HOJE":
        quo.speak_info_quotation()

    elif command_text == "COTAÇÃO DAS CRIPTOMOEDAS":
        quo.speak_crypto_info()

    elif command_text == "TRANSCREVA PARA MIM":
        transcribe.transcribe()

    elif command_text == "TRADUZA PARA MIM":
        transcribe.translate()

    elif command_text == "TWITTER":
        twitter.get_tweets()

    elif command_text == "NOTÍCIAS DO TWITTER":
        twitter.get_trending()

    elif command_text == "POSTAR NO TWITTER":
        twitter.post_tweet()

    elif command_text == "WIKIPÉDIA":
        tts.speak("Digite uma pesquisa")
        search_text = input("Digite uma pesquisa: ")
        tts.speak(wikipedia.get_wiki(search_text))

        #wikipedia.get_resume_wiki_page(search_text)

    elif command_text == "SAIR" or command_text == "DESLIGAR" or command_text == "PODE DESLIGAR":
        tts.speak("Me sinto grata por poder servir. Até mais!")
        sys.exit(0)
        break

    #break

print("fim")
