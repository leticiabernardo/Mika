__author__ = "foxx"
__email__ = "leticiaellenbernardo@gmail.com"
__version__ = "0.0.23"
__license__ = "MIT"
__status__ = "Beta"

from app.setup_tools.setup import Setup
# Setup()

print("Inicializando...")

import speech_recognition as sr
r = sr.Recognizer()

from app.command.basic import Basic
oran_says = Basic()

oran_says.hello()
oran_says.i_gonna_help_you()

my_command = ""
scout = 0

with sr.Microphone() as source:
    print("Diga algo...")

    r.adjust_for_ambient_noise(source, duration=0.02)
    while True:
        audio = r.listen(source)
        try:
            my_command += " " + r.recognize_google(audio, language='pt')
            scout = 0
        except sr.UnknownValueError:
            print("não entendi...")
            scout += 1
        except sr.Request as e:
            print("Oh no, something is wrong!\n" +
                  "I need to be fixed, tips: {0}".format(e))
            exit()

        print(my_command, scout)
        if scout == 1 and my_command != '':
            print("processando...")
            from app.query_sorter import QuerySorter
            q = QuerySorter(my_command)
            q.classifier()
            my_command = ""

        elif scout == 2:
            oran_says.i_cant_understand()

        elif scout == 4:
            oran_says.silence_mode()
