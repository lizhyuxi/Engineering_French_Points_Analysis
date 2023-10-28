############################################################
# GetTense class for determining which conjugation a verb is
# Example Usage:
#     GT = GetTense()
#     print(GT.get_tense('sais')) # [('savoir', 'indicative-present')]
#     print(GT.get_compound_verb('savoir')) # avoir
############################################################

import csv

class GetTense:
    def __init__(self, csv_path = None):
        if csv_path == None:
            slash = '/' if '/' in __file__ else '\\'
            ls = __file__.split(slash)[:-1]
            if ls[-1] == 'process_verb': ls = ls[:-1]
            if ls[-1] == 'programs': ls = ls[:-1]
            csv_path = slash.join(ls + ['data', 'french-verb-conjugation.csv'])
        self.tenses = {}
        self.compound = {}

        reader = csv.reader(open(csv_path, 'r'))
        conjug_csv = [row for row in reader]
        rows, cols = len(conjug_csv), len(conjug_csv[0])

        tenses = ['-'.join(str.split('|')[:-1]) \
                    if '|' in str \
                    else str.replace(' ', '-') \
                for str in conjug_csv[0]]

        for i in range(1, rows):
            row = conjug_csv[i]
            verb = row[0]
            for j in range(0, cols):
                word = row[j]
                if j == 4:
                    if word == '': word = 'avoir'
                    self.compound[verb] = word
                elif word != '':
                    if word not in self.tenses:
                        self.tenses[word] = []
                    self.tenses[word].append((row[0], tenses[j]))

        for key in self.tenses:
            self.tenses[key] = list(set(self.tenses[key]))

        for key in self.compound:
            self.compound[key] = list(self.compound[key].split(';'))

    def _get_tenses_list(self, word):
        return self.tenses[word] if word in self.tenses else []

    def _get_past_participle(self, word):
        return [x for x in self._get_tenses_list(word) if x[1] == 'past-participle']

    def get_tenses(self, word):
        ret = self._get_tenses_list(word)
        for i in [-1, -2]:
            if len(word) + i > 0 and word[i:] in ['e', 's', 'es']:
                ret += self._get_past_participle(word[:i])
        return list(set(ret))

    def get_compound_verb(self, word):
        return self.compound[word]
