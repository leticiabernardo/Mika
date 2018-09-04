import playsound


class Player:

    @staticmethod
    def play(file):
        playsound.playsound(file, True)

