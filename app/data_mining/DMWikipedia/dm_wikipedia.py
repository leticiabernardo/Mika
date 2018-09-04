import wikipedia
import config
import re

from app.data_mining.summarize import Summarize
from utils.tts import Tts


class DMWikipedia:
    def __init__(self):
        self.summarize = Summarize()
        self.tts = Tts()

    @staticmethod
    def get_wiki(query):
        wikipedia.set_lang(config.GENERAL_LANG)
        title = wikipedia.search(query)[0]
        page = wikipedia.page(title)
        page = re.sub('==[^==]+?==', '', page.content)

        return page

    def get_resume_wiki_page(self, query):
        page_content = self.get_wiki(query)
        resume = self.summarize.summarization(page_content)
        self.tts.speak(resume)



        # wikipedia.set_lang("pt")
# print (wikipedia.summary("wikipedia"))
# dm = DM_Wikipedia()
# print(dm.get_wiki("linguagem natural"))