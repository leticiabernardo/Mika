import json

import requests

from utils.tts import Tts


def real_br_money_mask(my_value):
    a = '{:,.2f}'.format(float(my_value))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')


def real_br_crypto_mask(my_value):
    a = '{:,}'.format(float(my_value))
    b = a.replace(',', 'v')
    c = b.replace('.', ',')
    return c.replace('v', '.')


class Quotation:

    def __init__(self):
        self.tts = Tts()

    #nao está mais funcionando
    @staticmethod
    def get_quotation():
        try:
            request_data = requests.get('http://api.promasters.net.br/cotacao/v1/valores')
            quo_dict = json.loads(request_data.text)
            return quo_dict

        except requests.exceptions.RequestException:
            return "error"

    @staticmethod
    def quotation_crypto():
        try:
            request_data = requests.get('https://api.coinmarketcap.com/v1/ticker/?convert=brl&limit=3')
            quo_dict = json.loads(request_data.text)
            return quo_dict

        except requests.exceptions.RequestException:
            return "error"

    @staticmethod
    def quotation_crypto_specific(crypto_specific=""):
        try:
            request_data = requests.get('https://api.coinmarketcap.com/v1/ticker/' + crypto_specific + "/?convert=brl")
            quo_dict = json.loads(request_data.text)
            return quo_dict

        except requests.exceptions.RequestException:
            return "error"

    # nao está mais funcionando
    def speak_info_quotation(self):
        quotation = self.get_quotation()

        if quotation == "error":
            self.tts.speak("Houve um erro ao acessar a quotação. Vamos tentar mais tarde?")
        else:
            dollar_value = real_br_money_mask(quotation['valores']['USD']['valor'])
            euro_value = real_br_money_mask(quotation['valores']['EUR']['valor'])
            #btc_value = real_br_money_mask(quotation['valores']['BTC']['valor'])

            self.tts.speak("A cotação do dólar hoje é de " + str(dollar_value) + " reais")
            self.tts.speak("Já a cotação do euro é de " + str(euro_value) + " reais")
            #self.tts.speak("E o Bitcoin é de " + str(btc_value) + " reais")

    def speak_crypto_info(self):
        quotation = self.quotation_crypto()

        if 'error' in quotation:
            self.tts.speak("Desculpe, não foi possível te trazer as informações. Vamos tentar mais tarde")
        else:
            self.tts.speak("As 3 maiores cripto moedas no momento são: ")

            for crypto_currency in quotation:

                crypto_name = crypto_currency['name']
                rank = crypto_currency['rank']
                price_usd = real_br_crypto_mask(crypto_currency['price_usd'])
                price_brl = real_br_crypto_mask(crypto_currency['price_brl'])
                percent_change_24h = crypto_currency['percent_change_24h']

                self.tts.speak("A moeda " + crypto_name + "é a " + rank + "ª no ranking")
                self.tts.speak("Seu valor está em " + price_usd + " dólares")
                self.tts.speak("e em " + price_brl + " reais")

                if float(percent_change_24h) > 0.0:
                    self.tts.speak("Houve um aumento de " + percent_change_24h + "% nas últimas 24h")
                else:
                    self.tts.speak("Houve um declínio de " + percent_change_24h + "% nas últimas 24h")

    def speak_crypto_info_details(self, crypto):
        crypto_currency = self.quotation_crypto_specific(crypto)

        if 'error' in crypto_currency:
            self.tts.speak("Desculpe, não foi possível te trazer as informações. Vamos tentar mais tarde")
        else:
            crypto_name = crypto_currency[0]['name']
            rank = crypto_currency[0]['rank']

            price_usd = real_br_crypto_mask(crypto_currency[0]['price_usd'])
            price_brl = real_br_crypto_mask(crypto_currency[0]['price_brl'])
            volume_usd_24h = real_br_money_mask(crypto_currency[0]['24h_volume_usd'])
            volume_brl_24h = real_br_money_mask(crypto_currency[0]['24h_volume_brl'])
            market_cap_usd = real_br_money_mask(crypto_currency[0]['market_cap_usd'])
            percent_change_24h = crypto_currency[0]['percent_change_24h']

            self.tts.speak("A cripto moeda " + crypto_name + "é a " + rank + "ª no ranking das cripto moedas no mercado")
            self.tts.speak("Seu valor atual é de " + price_usd + " dólares")
            self.tts.speak("Em reais, seu valor é de " + price_brl + " reais")

            if float(percent_change_24h) > 0.0:
                self.tts.speak("Houve um aumento de " + percent_change_24h + "% nas últimas 24h")
            else:
                self.tts.speak("Houve um declínio de " + percent_change_24h + "% nas últimas 24h")

            self.tts.speak("O volume em reais nas 24 horas foi de " + volume_brl_24h)
            self.tts.speak(" sendo que o volume total foi de " + volume_usd_24h)
            self.tts.speak("O total do mercado capital investido nesta moeda é de " + market_cap_usd + " dólares")
