import re


class Dictionary:
    def __init__(self):
        self.folder = "../../files/vocabulary/"
        self.save_folder = "dictionary/"
        self.folder_dic = "words/"
        self.words_name = "words_pt"
        self.words_synonymous = "base_tep2"
        self.extension = ".txt"
        self.file_name = "dic"
        self.effective_word_count = 0

    def create_dictionary(self):
        # file = open(self.folder + self.folder_dic + self.words_name + self.extension, "r")
        # dict_all = file.read()
        # file.close()

        # self.__create_dict_personal_names(dict_all)
        # self.dict_synonymous()








    @staticmethod
    def __regex(regex, str):
        regexp_handler = re.compile(regex)
        result = regexp_handler.search(str)
        return result.groups()[0]


    def __create_dict_personal_names(self, dict_all):
        dict_all_list = dict_all.strip().split('\n')
        dict_total = len(dict_all_list)
        valid_dict = []
        expressive_count = 0

        for num in range(dict_total):
            if dict_all_list[num][0].isupper():
                valid_dict.append(dict_all_list[num] + "\n")
                expressive_count += 1
            else:
                break

        str = ''.join(valid_dict)
        f = open(self.folder + self.save_folder + "NP/" + self.file_name + self.extension, "w")
        f.write(str)
        f.close()

        print("Palavras salvas:\n", valid_dict)
        print(expressive_count)

    def dict_synonymous(self):
        file = open(self.folder + self.folder_dic + self.words_synonymous + self.extension, "r")
        dict_synonymous_doc = file.read()
        file.close()

        dict_all_list = dict_synonymous_doc.strip().split('\n')

        vb = ""
        adj = ""
        adv = ""
        sb = ""
        for word in dict_all_list:
            regex = r"\[(.*?)\]"
            gramatical_class = self.__regex(regex, word)

            regex_2 = r"{(.*?)}"
            regex_match_2 = self.__regex(regex_2, word)

            words_list = regex_match_2.split(", ")

            str = words_list[0]

            if gramatical_class == 'Verbo':
                synonymous = ', '.join(words_list[1:])
                vb += str + "\n" if synonymous == "" else str + ":" + synonymous + "\n"
            elif gramatical_class == 'Adjetivo':
                synonymous = ', '.join(words_list[1:])
                adj += str + "\n" if synonymous == "" else str + ":" + synonymous + "\n"
            elif gramatical_class == 'Advérbio':
                synonymous = ', '.join(words_list[1:])
                adv += str + "\n" if synonymous == "" else str + ":" + synonymous + "\n"
            elif gramatical_class == 'Substantivo':
                synonymous = ', '.join(words_list[1:])
                sb += str + "\n" if synonymous == "" else str + ":" + synonymous + "\n"

        vb = '\n'.join(sorted(vb.split('\n')))
        adj = '\n'.join(sorted(adj.split('\n')))
        adv = '\n'.join(sorted(adv.split('\n')))
        sb = '\n'.join(sorted(sb.split('\n')))

        f = open(self.folder + self.save_folder + "VB/" + self.file_name + self.extension, "w")
        f.write(vb)
        f.close()

        f = open(self.folder + self.save_folder + "ADJ/" + self.file_name + self.extension, "w")
        f.write(adj)
        f.close()

        f = open(self.folder + self.save_folder + "ADV/" + self.file_name + self.extension, "w")
        f.write(adv)
        f.close()

        f = open(self.folder + self.save_folder + "SB/" + self.file_name + self.extension, "w")
        f.write(sb)
        f.close()



d = Dictionary()
d.create_dictionary()
