import os, codecs

class OutputFile: # A class for better output
    def __init__(self, name): # Initializing: output to file with name
        self.out = codecs.open(name, 'w', 'utf-8')
        self.lines = []
        self.indices = []

    def write(self, i, line): # Write a new line
        if len(self.lines) == 0 or self.lines[-1][0] != i:
            self.lines.append((i, line))

    def remove(self, i): # Remove the line with verb index = i
        for j in range(len(self.lines)):
            if self.lines[j][0] == i:
                self.lines.pop(j)
                return True
        return False

    def pop(self): # Remove the last line
        ret = self.lines[-1][0]
        self.lines.pop()
        return ret

    def __del__(self): # When deconstructing, output the data to the file
        self.out.write('\n\n'.join([str(len(self.lines))] +
            [self.lines[i][1] for i in range(len(self.lines))]))

class Output:
    def __init__(self, out_name, text):
        try:
            os.mkdir(out_name)
            os.mkdir(out_name + '/tmp')
        except:
            pass
        self.dict = { # Each tense and its corresponding output file name
            'ind_pre': 'indicatif-present',
            'inf': 'infinitif',
            'fut_sim': 'indicatif-futur-simple',
            'impar': 'indicatif-imparfait',
            'sub_pre': 'subjonctif-present',
            'con_pre': 'conditionnel-present',
            'par_pre': 'participe-present',
            'par_pas': 'participe-passe',
            'imper': 'imperatif-present',

            'fut_pro': 'indicatif-futur-proche',

            'pas_cop': 'indicatif-passe-compose',
            'plu_par': 'indicatif-plus-que-parfait',
            'fut_ant': 'indicatif-futur-anterieur',
            'sub_pas': 'subjonctif-passe',
            'con_pas': 'conditionnel-passe',

            'else': 'tmp/else'
        }
        self.sent = { # The dictionary for each corresponding OutputFile
            key: OutputFile(out_name + '/' + value + '.md') \
                    for key, value in self.dict.items()
        }
        self.tenses = [set() for _ in range(len(text))] # Each word corresponds to which tenses
        self.text = text

    # Get the full sentence which contains the i-th word
    def sent_contain(self, i):
        res = '**' + str(i) + '**:'
        j = i
        while i >= 0 and self.text[i][0] != '.':
            i -= 1
        st = i # The start of this sentence
        while True:
            i += 1
            if self.text[i][0] == '.': break
            res += ' '
            if i == j: res += '***' # Highlight this verb
            res += self.text[i][0]
            if i == j: res += '***' # Highlight this verb
        ed = i # The end of this sentence
        return res, st, ed

    def write(self, tense, i): # Set the i-th word as tense
        self.tenses[i].add(tense)
        self.sent[tense].write(i, self.sent_contain(i)[0])

    def remove(self, tense, i): # Remove the i-th word from tense
        if self.sent[tense].remove(i):
            self.tenses[i].remove(tense)

    def pop(self, tense): # Pop the last sentence from tense
        self.tenses[self.sent[tense].pop()].remove(tense)
