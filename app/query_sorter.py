import utils.helpers as Helpers


class QuerySorter:
    def __init__(self, query):
        self.query = Helpers.clean_word(query)

    def classifier(self):
        print(self.query)
        search_command = self.search_commands()

        if search_command is False:
            self.call_chatbot()

    def search_commands(self):
        if self.query in ["ORAN"]:
            from app.command.oran import Oran
            return Oran().call_my_name()

        elif self.query in ["PESQUISAR NO GOOGLE"]:
            from app.command.searchweb import SearchWeb
            return SearchWeb().search_in_gooogle()

        elif self.query in ["ABRIR SITE"]:
            from app.command.searchweb import SearchWeb
            return SearchWeb().search_site()

        elif self.query in ["QUE HORAS SÃO"]:
            from app.command.datetime import ComDateTime
            return ComDateTime().getTime()

        elif self.query in ["QUE DIA É HOJE"]:
            from app.command.datetime import ComDateTime
            return ComDateTime().getDate()

        elif self.query in ["COMO ESTÁ O TEMPO"]:
            from app.command.meteorology import Meteorology
            return Meteorology().getMeteorology()

        elif self.query in ["COMO ESTÁ A COTAÇÃO HOJE"]:
            from app.command.quotation import Quotation
            return Quotation().speak_info_quotation()

        elif self.query in ["COTAÇÃO DAS CRIPTOMOEDAS"]:
            from app.command.quotation import Quotation
            return Quotation().speak_crypto_info()

        elif self.query in ["TRANSCREVA PARA MIM"]:
            from app.command.transcribe import Transcribe
            return Transcribe().transcribe()

        elif self.query in ["TRADUZA PARA MIM"]:
            from app.command.transcribe import Transcribe
            return Transcribe().translate()

        elif self.query in ["TWITTER"]:
            from app.data_mining.DMTwitter.dm_twitter import DMTwitter
            return DMTwitter().get_tweets()

        elif self.query in ["NOTÍCIAS DO TWITTER"]:
            from app.data_mining.DMTwitter.dm_twitter import DMTwitter
            return DMTwitter().get_trending()

        elif self.query in ["POSTAR NO TWITTER"]:
            from app.data_mining.DMTwitter.dm_twitter import DMTwitter
            return DMTwitter().post_tweet()

        elif self.query in ["WIKIPÉDIA"]:
            from app.data_mining.DMWikipedia.dm_wikipedia import DMWikipedia
            return DMWikipedia().speak_wikipedia_page()

        elif self.query in ["SAIR", "DESLIGAR", "PODE DESLIGAR"]:
            from app.command.basic import Basic
            return Basic().goodbye()

        else:
            return False

    def call_chatbot(self):
        from app.chatbot.chatbot import Chatbot
        return Chatbot(self.query).initialize()
