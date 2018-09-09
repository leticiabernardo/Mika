from datetime import datetime
from pytz import timezone
from utils.tts import Tts


class ComDateTime:
    def __init__(self):
        self.tts = Tts()

    def getTime(self):
        south_africa = timezone('America/Sao_Paulo')
        sa_time = datetime.now(south_africa)

        self.tts.speak("Agora são " + sa_time.strftime('%H:%M'))

    #verificar timezone
    def getDate(self):
        america_timezone = timezone('America/Sao_Paulo')
        sa_time = datetime.now(america_timezone)

        print(sa_time)
        day_of_week = sa_time.strftime('%A')
        day = sa_time.strftime('%d')
        month = sa_time.strftime('%B')
        year = sa_time.strftime('%Y')

        self.tts.speak("Hoje é  " + day_of_week + ", dia" + day + " de " + month + " de " + year)