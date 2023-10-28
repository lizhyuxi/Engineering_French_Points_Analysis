#########################################################
# Expand l'élision
# For example: C'est => Ce est
# All l' will be expanded to le instead of la
# Usage: python3 elision.py $(input_txt_file_name) $(output_txt_file_name)

import re

list = ['ne']
full_list = []

for word in list:
    full_list.append(word)
    full_list.append(word[0].upper() + word[1:])

def expand_elision(text):
    # Expand s'il
    text = re.sub('S\'il', 'Si il', text)
    text = re.sub('s\'il', 'si il', text)

    for word in full_list:
        text = re.sub(word[:-1] + '\'', word + ' ', text)
    return text

if __name__ == '__main__':
    import sys, codecs
    assert(len(sys.argv) == 3)

    inp_name, out_name = sys.argv[1:3]

    inp = codecs.open(inp_name, 'r', 'utf-8')
    out = codecs.open(out_name, 'w', 'utf-8')

    out.write(expand_elision(str(inp.read())))
