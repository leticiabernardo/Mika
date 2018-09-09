class WordsClassifier:
    def __init__(self, str1, str2):
        self.path_dict = "files/vocabulary/"
        self.word_type = ""
        self.str1 = str1
        self.str2 = str2
        self.len_str1 = len(str1)
        self.len_str2 = len(str2)

    def validate_comparison(self):
        if self.percent_string_classification() > 0.76:
            return True

    def percent_string_classification(self):
        if self.basic_string_comparison():
            return 1
        if (len(max([self.str1, self.str2], key=len))
                - self.levenshtein_distance(self.str1, self.str2)) \
                / len(max([self.str1, self.str2], key=len)) > 0.65:
            return 1
        else:
            return "xiii"

    def basic_string_comparison(self):
        return self.str1 == self.str2


    def break_words(self):
        return True


    def search_synonymous(self):
        return True

    def levenshtein_distance(self, str1, str2):
        d = dict()
        for i in range(len(str1) + 1):
            d[i] = dict()
            d[i][0] = i
        for i in range(len(str2) + 1):
            d[0][i] = i
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                d[i][j] = min(d[i][j - 1] + 1, d[i - 1][j] + 1, d[i - 1][j - 1] + (not str1[i - 1] == str2[j - 1]))
        return d[len(str1)][len(str2)]


d = WordsClassifier("quero buscar no google", "buscar no google")
ret = d.percent_string_classification()
print(ret)
# print(len(max(["eu gostaria de fazer uma busca no google", "buscar no google"], key=len)))
# ret = d.levenshtein_distance("buscar na google", "busca no googles")

# print(len("eu gostaria de fazer uma busca no google"))

