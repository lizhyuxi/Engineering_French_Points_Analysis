# -*- coding: utf-8 -*-
#########################################################
# Process tag file and find all the modes and tenses for each verb
# Output to markdown files
# Usage: python3 process_tag.py $(input_tag_file_name) $(output_directory)
#########################################################

import sys, codecs
import re
from output import Output

### Files processing
assert(len(sys.argv) == 3)
inp_name, out_name = sys.argv[1:]

inp = codecs.open(inp_name, 'r', 'utf-8')

### Read text
text = []
lines = inp.readlines()
for line in lines:
    text.append(line.strip('\n').split(' '))

### Initialize output
out = Output(out_name, text)

def process_word(i): # Return the word with only lowercase letters
    word = text[i][0].lower()
    word = re.sub('[^a-zéàèùâêîôûçëïü]', '', word)
    return word

def find_before(i, word):
    if type(word) == type(''):
        word = [word]
    j = i
    while j > 0:
        j -= 1
        if text[j][0] == '.' or text[j][0][0].isupper():
            break
        if text[j][0] in word:
            return True
    return False

def is_subjonctif(i):
    if text[i][0].lower() in ['soit', 'soient']:
        return True
    return find_before(i, 'que')

from get_tense import GetTense

GT = GetTense()

# List of tenses which have unique conjugations
dict1 = {
    'indicative-future': 'fut_sim',
    'indicative-imperfect': 'impar',
    'indicative-conditional': 'con_pre',
    'present-participle': 'par_pre'
}

dict2 = {
    'pas_cop': 'ind_pre',
    'plu_par': 'impar',
    'fut_ant': 'fut_sim',
    'sub_pas': 'sub_pre',
    'con_pas': 'con_pre'
}

# List of indices for all verbs
idx = list(filter(lambda i : text[i][1] in ['VERB', 'AUX'] \
        or text[i][0][0].isupper() and text[i][0] != '.' \
        or text[i][0][0:3] == 'soi', range(len(text))))

infinitives = [set() for _ in range(len(text))]

determined = [tuple() for _ in range(len(text))]
try:
    with open(out_name + '/tmp/determined.txt', 'r') as inp: # Process those whose tense is already determined
        for line in inp.readlines():
            words = line.strip('\n').split(' ')
            i = int(words[0])
            determined[i] = tuple(words[1:])
            if i not in idx: idx.append(i)
except:
    pass

def confirm_tense(i, tense, infinitive):
    global flag
    if tense != 'else': infinitives[i].add(infinitive)
    out.write(tense, i)
    flag = True

id = -1
while True:
    id += 1
    if id == len(idx): break
    i = idx[id]
    lst_i = idx[id - 1] if id > 0 else -100
    print('\rProcessing ', id * 100 // len(idx), '%...', sep = '', end = '')

    if len(determined[i]) > 0:
        if len(determined[i]) == 1:
            text[i][1] = determined[i][0]
        else:
            tense, infinitive = determined[i]
            confirm_tense(i, tense, infinitive)
            # Check whether this tense is composé
            if tense in dict2:
                out.pop(dict2[tense])
        continue

    word = process_word(i) # the clean form of this verb

    # Get all possible modes and tenses of this verb
    tenses = GT.get_tenses(word)
    flag = False # whether it has a tense or not

    # Check whether it's the beginning of a sentence
    if text[i][0][0].isupper() and text[i][1] not in {'VERB', 'AUX'}:
        for a, b in tenses:
            if b == 'imperative':
                if word[-3:] == 'ons' or word[-2:] == 'ez':
                    confirm_tense(i, 'imper', a)
                else:
                    confirm_tense(i, 'else', a)
            elif b == 'subjunctive-present' and a == 'être' \
                    and is_subjonctif(i):
                confirm_tense(i, 'sub_pre', a)
        continue

    else:
        for a, b in tenses: # Check each possible tenses
            if b in dict1:
                confirm_tense(i, dict1[b], a)
            if b == 'indicative-present':
                confirm_tense(i, 'ind_pre', a)
                if a == 'aller' and i + 1 not in idx:
                    idx.insert(id + 1, i + 1)
            elif b == 'infinitive':
                if lst_i > i - 3 and 'aller' in infinitives[lst_i]:
                    out.pop('ind_pre')
                    confirm_tense(i, 'fut_pro', a)
                else:
                    confirm_tense(i, 'inf', a)
            elif b == 'past-participle' and text[i - 1][2] != 'on': # All the composé forms
                flag = False
                if lst_i > i - 3:
                    for compound in GT.get_compound_verb(a):
                        if compound in infinitives[lst_i]:
                            for this_tense, last_tense in dict2.items():
                                # this_tense means the auxilary verb should
                                # be in the form of last_tense
                                if last_tense in out.tenses[lst_i]:
                                    # If compound is 'être', this verb can be a pass participle
                                    # Otherwise, the compound 'avoir' must be an auxilary verb
                                    if compound == 'avoir':
                                        out.remove(last_tense, lst_i)
                                    confirm_tense(i, this_tense, a)
                if not flag or 'être' in infinitives[lst_i]:
                    confirm_tense(i, 'par_pas', a)
            elif b == 'subjunctive-present':
                if is_subjonctif(i):
                    confirm_tense(i, 'sub_pre', a)
    # if not flag and text[i][1] == 'VERB':
    #    out.write('else', i) # No tenses are available, probably a not a verb

print('\rDone                    \n')

for i in range(len(text)):
    if text[i][2] == 'que' and 'montrer' in infinitives[i - 1]:
        text[i][1] = 'SCONJ'
    elif text[i][0] == 'au' and text[i][1] == 'ADP':
        text[i][2] = 'à'

appear = {}

for i in range(len(text)):
    for s in infinitives[i]:
        if s not in appear: appear[s] = 0
        appear[s] += 1

undetermined = []

for i in range(len(text)):
    if len(infinitives[i]) > 0:
        mx = (0, 0)
        for s in infinitives[i]:
            tup = (appear[s], s)
            if tup > mx: mx = tup
        cnt = 0
        for s in infinitives[i]:
            if appear[s] == mx: cnt += 1
        text[i][1] = 'VERB'
        text[i][2] = mx[1]
        if cnt > 1: print('alert, multiple infinitives', infinitives[i])
        if len(list(out.tenses[i])) > 1 or cnt > 1:
            undetermined.append(i)

with codecs.open(out_name + '/new_tag.txt', 'w', 'utf-8') as f:
    f.write('\n'.join([' '.join(text[i] + list(out.tenses[i])) for i in range(len(text))]))

with codecs.open(out_name + '/tmp/undetermined.md', 'w', 'utf-8') as f:
    f.write(str(len(undetermined)) + '\n\n')
    for i in undetermined:
        f.write(out.sent_contain(i)[0] + '\n\n')
        f.write(' '.join(list(out.tenses[i])) + '\n\n')
