import requests
from bs4 import BeautifulSoup
import json

try:
    page = requests.get('https://lifestyle.sapo.pt/astral/previsoes/maya?signo=capricornio')

    soup = BeautifulSoup(page.content, 'html.parser')
    #body = list(soup.children)[2]
    textooo = soup.find_all('div', class_='horoscope-text')[1].get_text()

    p_tags = soup.find_all('div', class_='horoscope-text')[1]
    for x in range(len(p_tags)):
        print("{}: {}".format(p_tags[x].string, p_tags[x].string))

    #paragrafos = soup.findChildren('div', class_='horoscope-text')
    print(textooo)

    #print (textooo)


except Exception as e:
    print("Requisição com erro", e)