import json

import requests
from googletrans import Translator

from utils.tts import Tts


def i18n_weather(sky):
    if sky == "Clear":
        return "limpo"
    elif sky == "Clouds":
        return "nublado"
    elif sky == "Rain":
        return "chuvoso"
    elif sky == "Drizzle":
        return "chuviscando"
    else:
        return ''


class Meteorology:
    def __init__(self):
        self.city = "Americana"
        self.app_id = "044f0c71f29021e618fcb5eadb866017"
        self.tts = Tts()
        self.translator = Translator()

    def getMeteorology(self):
        request = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + self.city + "&appid=" + self.app_id)

        meteorology = json.loads(request.text)

        weather = meteorology['weather']
        weather_main = meteorology['main']

        temperature = '{:,.1f}'.format(float(weather_main['temp']) - 273.15)
        temp_min = '{:,.1f}'.format(float(weather_main['temp_min']) - 273.15)
        temp_max = '{:,.1f}'.format(float(weather_main['temp_max']) - 273.15)
        humidity = weather_main['humidity']

        sky = weather[0]['main']
        desc = weather[0]['main']

        sky_pt = i18n_weather(sky)

        if sky_pt == '':
            sky_pt = (self.translator.translate(sky, dest='pt')).text

        translate_desc = self.translator.translate(desc, dest='pt')

        self.tts.speak("O tempo em " + self.city + " está" + sky_pt + " com " + translate_desc.text)
        self.tts.speak("A temperatura agora é de {}" + temperature + " graus")
        self.tts.speak("A mínima para hoje é de " + temp_min)
        self.tts.speak("E a máxima de " + temp_max + " graus")
        self.tts.speak("A umidade do ar chega aos " + str(humidity) + "%")
