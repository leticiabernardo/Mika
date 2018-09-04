from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest


class Summarize:

    @staticmethod
    def summarization(text):
        text_sentences = sent_tokenize(text)
        text_words = word_tokenize(text.lower())
        stop_words = set(stopwords.words('portuguese') + list(punctuation))
        stopwords_list = [word for word in text_words if word not in stop_words]

        frequency = FreqDist(stopwords_list)
        important_sentences = defaultdict(int)

        for i, text_sentence in enumerate(text_sentences):
            for word in word_tokenize(text_sentence.lower()):
                if word in frequency:
                    important_sentences[i] += frequency[word]

        idx_important_sentences = nlargest(4, important_sentences, important_sentences.get)

        final_text = ""
        for i in sorted(idx_important_sentences):
            final_text = text_sentences[i]

        return final_text
